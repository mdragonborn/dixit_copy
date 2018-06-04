from django.contrib.auth.forms import UserCreationForm
from profiles.models import Player, Avatar
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = Player
        fields = ('username', 'email', 'password1', 'password2')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', 'codename',)