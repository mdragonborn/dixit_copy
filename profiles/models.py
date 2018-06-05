from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Avatar(models.Model):
    # TODO: Replace placeholder paths.
    image = models.ImageField(upload_to='avatars')
    codename = models.CharField(max_length=100, unique=True)


DEFAULT_AVATAR_ID = 1  # TODO: Replace with natural key.


class Constant(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField()


class Color(Constant):
    pass


class AliasField(models.Field):
    def contribute_to_class(self, cls, name, private_only=False):
        super().contribute_to_class(cls, name, private_only=True)
        setattr(cls, name, self)

    def __get__(self, instance, instance_type=None):
        return getattr(instance, self.db_column)

    def __set__(self, instance, value):
        setattr(instance, self.db_column, value)


class Player(AbstractUser):
    avatar = models.ForeignKey(Avatar, on_delete=models.SET_DEFAULT,
                               default=DEFAULT_AVATAR_ID)
    profile_picture = models.ImageField(upload_to='profile_pictures',
                                        default='profile_pictures/default.png')
    is_vip = models.BooleanField(default=False)
    vip_expiry = models.DateTimeField(null=True)
    is_admin = AliasField(db_column='is_staff')


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
