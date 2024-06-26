from django import forms
from .models import Player, Team

class PlayerForm(forms.ModelForm):
    
    class Meta:
        model = Player
        #fields = ('playername', 'noofmatches', 'runsscored', 'noofsixes', 'nooffours','strikerate', 'noofwickets', 'economy', 'bestbowling')
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('user', None)
        super(PlayerForm, self).__init__(*args, **kwargs)
        teamids = Team.objects.filter(teamname=current_user.teamname)
        self.fields['teamid'].queryset = teamids
        
