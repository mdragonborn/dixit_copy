from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .models import Player
from .forms import SignUpForm

def profile(request):
    player = Player.create_user(username="qwe0", email="123@qwe.rt", password="bozidar", first_name="bozidar", last_name="takodje")
    if player is None:
        return HttpResponse("ummmm")
    else:
        return HttpResponse(player.User.username)

def index(request):
    return HttpResponse("index?")


def signup(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('home')
    # else:
    #     form = SignUpForm()
    #return render(request, 'profiles/signup.html', {'form': form})

    return render(request, 'profiles/signup.html')