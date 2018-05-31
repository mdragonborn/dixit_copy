from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Avatar(models.Model):
    # TODO: Replace placeholder paths.
    image = models.ImageField(upload_to='avatars')
    codename = models.CharField(max_length=100, unique=True)


DEFAULT_AVATAR = Avatar(image='default.png', codename='default')


class Constant(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField()


class Color(Constant):
    pass


class Player(AbstractUser):
    avatar = models.ForeignKey(Avatar, on_delete=models.SET_DEFAULT,
                               default=DEFAULT_AVATAR)
    profile_picture = models.ImageField(upload_to='profile_pictures',
                                        default='profile_pictures/default.png')
    is_vip = models.BooleanField(default=False)
    vip_expiry = models.DateTimeField(null=True)
    is_admin = AbstractUser.is_staff


class AchievementType(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=100, unique=True)


class Achievement(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    achievement_type = models.ForeignKey(AchievementType, on_delete=models.CASCADE)
    value = models.FloatField()

    class Meta:
        unique_together = ('player', 'achievement_type')


class Expansion(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='expansions',
                              default='expansions/default.png')
    codename = models.CharField(max_length=100, unique=True)


class Card(models.Model):
    expansion = models.ForeignKey(Expansion, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='cards',
                              default='cards/default.jpg')
    codename = models.CharField(max_length=100, unique=True)
