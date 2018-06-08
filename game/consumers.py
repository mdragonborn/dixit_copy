import re
import logging
from channels import Group
from channels.sessions import channel_session
from .game import Game
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
log = logging.getLogger(__name__)
from django.utils.decorators import method_decorator
from django.core.cache import cache

from channels.generic.websockets import JsonWebsocketConsumer

class GameConsumer(JsonWebsocketConsumer):
    http_user = True

    def connection_groups(selfself, **kwargs):
        return ["game-{0}".format(kwargs['game_id'])]

    def connect(self, mssage, **kwargs):
        pass

    def receive(self, content, **kwargs):
        channel_session_user = True
        action = content['action']
        print("ACTION {0}".format(action))

        print(action)

    def disconnect(selfself, message, **kwargs):

        pass
