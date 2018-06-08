from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, ImageForm


def home(request):
    return render(request, 'authenticate/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    form = SignUpForm()
    return render(request, 'authenticate/signup.html', {'form': form})


def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = ImageForm()
    return render(request, 'authenticate/model_form_upload.html', {'form': form})
