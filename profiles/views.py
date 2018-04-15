from django.http import HttpResponse
from django.shortcuts import render

from .models import Player
from django.contrib.auth.models import User

def profile(request):
    player = Player.create_user(username="qwe0", email="123@qwe.rt", password="bozidar", firstname="bozidar", lastname="takodje")
    if player is None:
        return HttpResponse("ummmm")
    else:
        return HttpResponse(player.User.username)

def index(request):
    return HttpResponse("index?")