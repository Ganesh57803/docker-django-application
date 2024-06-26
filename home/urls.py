from django.urls import path
from .views import *


urlpatterns = [
    path("", currentMatches, name="home"),
    path("matches/", matches_view, name="matches"),
    path("teams/", team_list, name = "teams"),
    path("teams/<int:teamid>", teamsview, name = "teamsview"),
    path("points_table/", points_table, name = "points_table"),
    path("add_players/", add_players, name = "add_players"),
    path("update_players/<int:playerid>", update_players, name = "update_players"),
    path("delete_players/<int:playerid>", delete_players, name = "delete_players"),
    path("queryset/", queryset, name = "queryset"),
    
    

    

    
]
