from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from home.models import *

# Create your models here.
class TeamManager(AbstractUser):
    
    managername = models.CharField("Manager Name", db_column='ManagerName', max_length=30)  
    battingcoach = models.CharField(db_column='BattingCoach', max_length=30)  
    bowlingcoach = models.CharField(db_column='BowlingCoach', max_length=30)
    teamname = models.CharField("Team Name", db_column='TeamName', max_length=30)
    is_manager = models.BooleanField(default=True)

    REQUIRED_FIELDS = []


    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        super(TeamManager, self).save(*args, **kwargs)
    

    def __str__(self):  
        return self.managername