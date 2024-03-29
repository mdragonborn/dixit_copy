from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework import viewsets
from django.contrib import messages
from django.contrib.auth import get_user
from .game import Game

from dixit.models import Card
from dixit.serializers import CardSerializer
from .forms import ImageForm, CreateGameForm
import pickle
import redis

from dixit.settings import REDIS_HOST, REDIS_PORT

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
            redis_db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

            games = {}
            if (redis_db.get('available_games') is not None):
                games = pickle.loads(redis_db.get('available_games'))
            games[str(game.game_id)] = {'free_places': game.player_limit - 1, 'limit': game.player_limit}

            redis_db.set('available_games', pickle.dumps(games))
            print(game.game_id, game)
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
        redis_db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
        game_cache = redis_db.get(kwargs['game_id'])
        if not game_cache:
            messages.add_message(request, messages.ERROR, "soz")
            return redirect ('/lobby/')
        game_id = kwargs['game_id']

        # with cache._lock(game_id):
        user = get_user(request)
        game = None

        #
        # if game_cache is None:
        #     game = Game(user.id, 4)
        #     games = {}
        #     if(redis_db.get('available_games') is not None):
        #         games = pickle.loads(redis_db.get('available_games'))
        #     games[game_id]={'free_places': game.player_limit-1, 'limit': game.player_limit }
        #     redis_db.set('available_games', pickle.dumps(games))
        # else:
        game = pickle.loads(game_cache)
        print(game.players)
        if game.already_joined(user.id):
            return super(GameView, self).dispatch(request, *args, **kwargs)

        if game.is_available():
            result = game.add_player(user.id)
            if not result:
                messages.add_message(request, messages.ERROR, "nesto nece")
                return redirect('/lobby/')

            # with cache.lock('available_games'):
            games = pickle.loads(redis_db.get('available_games'))
            if game.has_started:
                games.pop(game_id)
            else:
                games[game_id]['free_places'] -= 1

            redis_db.set('available_games', pickle.dumps(games))
            redis_db.set(game_id, pickle.dumps(game))

            return super(GameView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('/lobby/')


    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)
        redis_db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
        print(self.game_id)
        if self.game_id is not None:
            game = redis_db.get(self.game_id)
            print(game)
            context['game'] = pickle.loads(game)
        return context
