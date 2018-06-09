from django.contrib.auth.forms import UserCreationForm
from dixit.models import Player, Avatar, Card, Expansion
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = Player
        fields = ('username', 'email', 'password1', 'password2')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('image', 'codename',)


IS_PRIVATE_CHOICES = [
    ('private', 'Private game'),
    ('public', 'Public game')
]

NUM_OF_PLAYERS_CHOICES = [
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6')
]


# TODO: Odkomentarisati kad se expansions stave u bazu
# EXPANSIONS_CHOICES = [(expansion.name, expansion.name) for expansion in Expansion.objects.all()]
EXPANSIONS_CHOICES = [
    ('daydreams', 'Dixit: Daydreams'),
    ('oddyssey', 'Dixit: Oddyssey')
]


class CreateGameForm(forms.Form):
    room_name = forms.CharField(label='Room name:', max_length=100)
    is_private = forms.ChoiceField(label='', widget=forms.RadioSelect, choices=IS_PRIVATE_CHOICES)
    card_pack = forms.ChoiceField(label='Card pack', widget=forms.Select, choices=EXPANSIONS_CHOICES)
    num_of_players = forms.ChoiceField(label='Number of players', widget=forms.Select, choices=NUM_OF_PLAYERS_CHOICES)
