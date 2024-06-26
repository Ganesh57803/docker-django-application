from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import *
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from datetime import date, datetime, timedelta
from django.db.models.signals import post_save
from accounts.models import TeamManager
from .forms import PlayerForm

class HomePageView(TemplateView):
    template_name = "home.html"

    def currentMatches(request):
        today = date.today()
        #current_matches = Matches.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)
        current_matches = Matches.objects.all()
        print(current_matches)
        return {'current_matches': current_matches}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_matches'] = self.currentMatches()
        return context

def currentMatches(request):
        today = date.today()
        yesterday = datetime.now() - timedelta(1)
        current_matches = Matches.objects.filter(mdate__year=today.year, mdate__month=today.month, mdate__day=today.day)
        #current_matches = Matches.objects.all()
        print(current_matches)
        last_match = Matches.objects.filter(mdate__year=yesterday.year, mdate__month=yesterday.month, mdate__day=yesterday.day)
        print(last_match)
        return render(request, "home.html", {'current_matches': current_matches, 'last_match': last_match[0] if last_match else last_match})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, username)
            return redirect('home')
        else:
            messages.warning(request, "Username or Password is incorrect")


def team_list(request):
    # cursor = connection.cursor
    # cursor.execute("SELECT * FROM TEAM")
    data = Team.objects.raw("SELECT * FROM team")
    print(data)
    print(connection.queries)
    return render(request, 'teams.html', {'teamslist': data})

def teamsview(request, teamid):
    if(Team.objects.filter(teamid=teamid)):
        players = Player.objects.filter(teamid=teamid)
        # players = Player.objects.filter(runsscored__lt=3000,teamid=teamid)
        
        context = {'players': players}
        return render(request, "team_details.html", context)
    else:
        messages.warning(request, "No such team found!")
        return redirect('teams')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def matches_view(request):
    matches = Matches.objects.raw("SELECT * from matches")
    return render(request, "matches.html", {'matches': matches})

def findTeamName(id):
    teamname = Team.objects.raw("Select teamname from team where teamid=id")
    return(teamname)



def update_points(sender, instance, **kwargs):
    print("Signal received!!!")
    if instance.result != 'D':
        if instance.result == 'A':
            winner = Team.objects.get(teamname = instance.teama_id)
            loser = Team.objects.get(teamname = instance.teamb_id)
        else:
            winner = Team.objects.get(teamname = instance.teamb_id)
            loser = Team.objects.get(teamname = instance.teama_id)
        # update_points = Team.objects.raw("update team set points=points+2 where teamname=%s", winner)
        # print(update_points)
        # w = Team.objects.get(teamname=winner.teamname)
        # w.points = w.points + 2
        # w.save()
        # print(w)
        winner.noofwins = winner.noofwins+1
        winner.points = winner.points+2
        winner.save(update_fields=["noofwins", "points"])

        loser.nooflosses = loser.nooflosses+1
        loser.save(update_fields=["nooflosses"])
        print(winner)
        print(loser)
    else:
        a = Team.objects.get(teamname=instance.teama_id)
        b = Team.objects.get(teamname=instance.teamb_id)
        a.points = a.points+1
        a.save(update_fields=["points"])
        b.points = b.points+1
        b.save(update_fields=["points"])
        print(a, b)

        

post_save.connect(update_points, sender=Matches)


def points_table(request):
    data = Team.objects.raw("Select * FROM team order by points desc")
    print(data)
    print(connection.queries)
    return render(request, 'points_table.html', {'teamslist': data})


def create_team_table_from_manager_info(sender, instance, created, **kwargs):
    print("manager signal received")
    if created:
        nt = Team(teamname=instance.teamname)
        nt.save()
        print(nt)

post_save.connect(create_team_table_from_manager_info, sender=TeamManager)


def add_players(request):
    
    form = PlayerForm(user=request.user)
    #form.fields['teamid'].initial = teamid
    #form.instance.teamid = form.cleaned_data['teamid'] = Team.objects.get(teamname=request.user.teamname)
    #form.fields['teamid'].widget.attrs['disabled'] = True
    if request.method == 'POST':
        print(request.POST)
        form = PlayerForm(request.POST or None, user = request.user)
        if form.is_valid():
            print('valid')                     
            form.save()
            messages.success(request, "Player added successfully")
        
    teamid = Team.objects.get(teamname=request.user.teamname).teamid
    playerlist = Player.objects.filter(teamid=teamid)

        
    return render(request, 'manager/dashboard.html', {'form': form, 'playerlist': playerlist})

def update_players(request, playerid):
    player = Player.objects.get(playerid=playerid)
    form = PlayerForm(instance=player, user=request.user)
    if request.method == 'POST':
        print(request.POST)
        form = PlayerForm(request.POST or None, user = request.user, instance=player)
        if form.is_valid():
            print('valid')                     
            form.save()
            messages.success(request, "Player updated successfully")
            return redirect('add_players')
    
    teamid = Team.objects.get(teamname=request.user.teamname).teamid
    playerlist = Player.objects.filter(teamid=teamid)
    return render(request, 'manager/dashboard.html', {'form': form, 'playerlist': playerlist })

def delete_players(request, playerid):
    player = Player.objects.get(playerid=playerid)
    
    if request.method == 'POST':                            
        player.delete()
        messages.success(request, "Player deleted successfully")
        return redirect('add_players')


    return render(request, 'manager/delete_player.html', {'player' : player})

def queryset(request):
    
        
    players = Player.objects.filter(runsscored__lt=3000)
        
    context = {'players': players}
    return render(request, "queryset.html", context)