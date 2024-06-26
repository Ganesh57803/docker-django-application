from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = TeamManager
    list_display = ['username','managername', 'is_staff', 'teamname', 'battingcoach','bowlingcoach']
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Team Management Info',
            {
                'fields':('managername', 'battingcoach', 'bowlingcoach', 'teamname')
            }
        )
    )

    

admin.site.register(TeamManager,CustomUserAdmin)
