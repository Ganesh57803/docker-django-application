from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = TeamManager
        fields = ['username', 'teamname', 'managername', 'battingcoach', 'bowlingcoach', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = TeamManager
        fields = ['username']