from django.shortcuts import render, redirect
from django.contrib.auth import login

from game.serializers import CardSerializer
from .forms import SignUpForm, ImageForm
from django.views.generic import TemplateView
from profiles.models import Card
from django.http import HttpResponse
from rest_framework import viewsets

def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ImageForm()
    return render(request, './model_form_upload.html', {
        'form': form
    })


class RetrieveImages(viewsets.ModelViewSet):
    queryset = Card.objects.get_queryset()
    serializer_class = CardSerializer


class GameView(TemplateView):
    template_name='components/game/index.html'