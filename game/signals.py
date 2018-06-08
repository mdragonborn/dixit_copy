from channels import Group
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import redis


@receiver(post_save)
def new_game_handler(**kwargs):
    if kwargs['created']:
        redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
        Group('lobby').send(redis_db.get('available_games'))  # redis vec cuva serijalizovano
