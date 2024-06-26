from django.urls import path
from .views import *

urlpatterns = [
    path("register/",registerPage, name="register")
]
