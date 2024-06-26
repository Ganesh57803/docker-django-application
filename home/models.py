# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)




class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Team(models.Model):
    teamid = models.AutoField(db_column='TeamID', primary_key=True)  # Field name made lowercase.
    teamname = models.CharField(db_column='TeamName', max_length=40, unique=True, null=False, blank=False)  # Field name made lowercase.
    #teamrank = models.IntegerField(db_column='TeamRank')  # Field name made lowercase.
    noofdraws = models.IntegerField(db_column='NoOfDraws', blank=True, null=True, default=0)  # Field name made lowercase.
    noofwins = models.IntegerField(db_column='NoOfWins', blank=True, null=True, default=0)  # Field name made lowercase.
    nooflosses = models.IntegerField(db_column='NoOfLosses', blank=True, null=True, default=0)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points', blank=True, null=True, default=0)  # Field name made lowercase.

    class Meta:
        db_table = 'team'
    
    def __str__(self):
        return self.teamname




class Matches(models.Model):
    
    RES = [
        ('A', 'Team A won'),
        ('B', 'Team B won'),
        ('D', 'Draw')]

    STAT = [
        ('O', 'Match over'),
        ('N', 'Match not over'),
        ('C', 'Cancelled/abandoned')
    ]

    matchid = models.AutoField(db_column='MatchID', primary_key=True)  # Field name made lowercase.
    teama_id = models.ForeignKey(Team, db_column='teamA_ID', related_name="teamA",on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    teamb_id = models.ForeignKey(Team, db_column='teamb_ID', related_name="teamB",on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, choices=STAT)  # Field name made lowercase.
    result = models.CharField(max_length=1, blank=True, null=True, choices=RES)
    location = models.CharField(db_column='Location', max_length=20)  # Field name made lowercase.
    mdate = models.DateField(db_column='Mdate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'matches'
        
    def save(self, *args, **kwargs):
        super(Matches, self).save(*args, **kwargs)
        

    def __str__(self):
        return str(self.matchid)


class Player(models.Model):
    playerid = models.AutoField(db_column='PlayerID', primary_key=True)  # Field name made lowercase.
    playername = models.CharField(db_column='PlayerName', max_length=30)  # Field name made lowercase.
    noofmatches = models.IntegerField(db_column='NoOfMatches', blank=True, null=True)  # Field name made lowercase.
    teamid = models.ForeignKey(Team, db_column='TeamID', on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    runsscored = models.IntegerField(db_column='RunsScored', blank=True, null=True)  # Field name made lowercase.
    noofsixes = models.IntegerField(db_column='NoOfSixes', blank=True, null=True)  # Field name made lowercase.
    strikerate = models.FloatField(db_column='StrikeRate', blank=True, null=True)  # Field name made lowercase.
    noofwickets = models.IntegerField(db_column='NoOfWickets', blank=True, null=True)  # Field name made lowercase.
    economy = models.FloatField(db_column='Economy', blank=True, null=True)  # Field name made lowercase.
    bestbowling = models.CharField(db_column='BestBowling', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nooffours = models.IntegerField(db_column='NoOfFours', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'player'
    
    def __str__(self):
        return self.playername


class Captain(models.Model):
    captainid = models.AutoField(db_column='CaptainID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey(Player, db_column='PlayerID', on_delete=models.CASCADE, null=True)
    noofmatches = models.IntegerField(db_column='NoOfMatches', blank=True, null=True)  # Field name made lowercase.
    noofwins = models.IntegerField(db_column='NoOfWins', blank=True, null=True)  # Field name made lowercase.
    teamid = models.ForeignKey(Team, db_column='teamID', on_delete=models.CASCADE)
      # Field name made lowercase.

    class Meta:
        db_table = 'captain'

    def __str__(self):
        return self.playerid.playername


class Plays(models.Model):
    teamid = models.IntegerField(Team, db_column='TeamID', primary_key=True)  # Field name made lowercase.
    matchid = models.ForeignKey(Matches, db_column='MatchID', on_delete=models.CASCADE, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'plays'
        unique_together = (('teamid', 'matchid'),)

    def __str__(self):
        return self.teamid





class Teammanagement(models.Model):
    managerid = models.AutoField(db_column='ManagerID', primary_key=True)  # Field name made lowercase.
    teamid = models.ForeignKey(Team, db_column='teamID', on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    managername = models.CharField(db_column='ManagerName', max_length=30)  # Field name made lowercase.
    battingcoach = models.CharField(db_column='BattingCoach', max_length=30)  # Field name made lowercase.
    bowlingcoach = models.CharField(db_column='BowlingCoach', max_length=30)  # Field name made lowercase.

    class Meta:        
        db_table = 'teammanagement'
    
    def __str__(self):
        return self.managername



class Umpire(models.Model):
    umpireid = models.AutoField(db_column='umpireID', primary_key=True)  # Field name made lowercase.
    umpirename = models.CharField(db_column='UmpireName', max_length=30)  # Field name made lowercase.
    noofmatches = models.IntegerField(db_column='NoOfMatches', blank=True, null=True)  # Field name made lowercase.

    class Meta:        
        db_table = 'umpire'
    
    def __str__(self):
        return self.umpirename



class Umpiredby(models.Model):
    matchid = models.IntegerField(Matches, db_column='MatchID', primary_key=True)  # Field name made lowercase.
    umpireid = models.ForeignKey(Umpire, db_column='UmpireID', on_delete=models.CASCADE, null=True)  # Field name made lowercase.

    class Meta:        
        db_table = 'umpiredby'
        unique_together = (('matchid', 'umpireid'),)
    
    def __str__(self):
        return self.matchid

