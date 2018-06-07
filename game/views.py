from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework import viewsets

from dixit.models import Card
from dixit.serializers import CardSerializer
from .forms import ImageForm

def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ImageForm()
    return render(request, 'cardupload/model_form_upload.html', {
        'form': form
    })


class RetrieveImages(viewsets.ModelViewSet):
    queryset = Card.objects.get_queryset()
    serializer_class = CardSerializer


class GameView(TemplateView):
    template_name='components/game/index.html'
