from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework import viewsets
from django.core.cache import cache
from django.contrib import messages
from django.contrib.auth import get_user
from .game import Game

from dixit.models import Card
from dixit.serializers import CardSerializer
from .forms import ImageForm, CreateGameForm
import pickle
from django.core.cache import cache

import redis


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


@login_required()
def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            game = Game(get_user(request).id, int(form.cleaned_data['num_of_players']))
            redis_db = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)

            games = {}
            if (redis_db.get('available_games') is not None):
                games = pickle.loads(redis_db.get('available_games'))
            games[form.cleaned_data['num_of_players']] = {'free_places': game.player_limit - 1, 'limit': game.player_limit}

            print(games)
            redis_db.set('available_games', pickle.dumps(games))

            print(game.game_id)
            redis_db.set(game.game_id, pickle.dumps(game))

            return redirect('/game/' + str(game.game_id))
    form = CreateGameForm()
    return render(request, 'create_game.html', {'form': form})


class RetrieveImages(viewsets.ModelViewSet):
    queryset = Card.objects.get_queryset()
    serializer_class = CardSerializer


class GameView(TemplateView):
    template_name = 'components/game/index.html'
    game = None
    game_id = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
        game_cache = redis_db.get(kwargs['game_id'])
        print(request.method)
        print("redis_db", game_cache)
        # if not game_cache:
        #     messages.add_message(request, messages.ERROR, "soz")
        #     return redirect ('/lobby/')
        game_id = kwargs['game_id']

        # with cache._lock(game_id):
        user = get_user(request)
        print(game_cache)
        game = None

        #
        if game_cache is None:
            game = Game(user.id, 4)
            games = {}
            if(redis_db.get('available_games') is not None):
                games = pickle.loads(redis_db.get('available_games'))
            games[game_id]={'free_places': game.player_limit-1, 'limit': game.player_limit }
            print(games)
            redis_db.set('available_games', pickle.dumps(games))
        else:
            game = pickle.loads(game_cache)

        if game.is_available():
            result = game.add_player(user.id)
            if not result:
                messages.add_message(request, messages.ERROR, "nesto nece")
                return redirect('/lobby/')

            # with cache.lock('available_games'):
            games = pickle.loads(redis_db.get('available_games'))
            print(games)
            if game.has_started:
                games.remove(game_id)
            else:
                games[game_id]['free_places'] -= 1

            # redis_db.set('available_games', pickle.dumps(games))
            redis_db.set(game_id, pickle.dumps(game))
        return super(GameView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)
        context['game'] = self.game
        return context
