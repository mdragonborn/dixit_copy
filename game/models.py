from django.db import models
import dixit.models as dixit_models

class Game(models.Model):
    has_ended = models.BooleanField(default=False)
    player_1 = models.ForeignKey(null=False)
    player_2 = models.ForeignKey()
