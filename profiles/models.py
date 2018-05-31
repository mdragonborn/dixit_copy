from django.contrib.auth.models import User
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


# TODO: Check if it would be better to inherit from AbstractUser instead.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ForeignKey(Avatar, on_delete=models.SET_DEFAULT,
                               default=DEFAULT_AVATAR)
    profile_picture = models.ImageField(upload_to='profile_pictures',
                                        default='profile_pictures/default.png')
    is_vip = models.BooleanField(default=False)
    vip_expiry = models.DateTimeField(null=True)

    @property
    def is_admin(self):
        return self.user.is_staff

    # TODO: User creation hooks etc.

    # @staticmethod
    # def create_user(username, first_name, last_name, email, password):
    #     if User.objects.filter(username=username, email=email).exists():
    #         return None
    #     else:
    #         player = Player(user=User.objects.create_user(username, email, password))
    #         player.user.first_name = first_name
    #         player.user.last_name = last_name
    #         Player.save(player)
    #         return player
    #
    # @staticmethod
    # def does_user_exist(username, email):
    #     if User.objects.filter(username=username, email=email).exists():
    #         return None
    #     return User.objects.filter(username=username, email=email)
    #     # @staticmethod
    #     # def create_admin():
    #
    #     # get_absolute_url ?


class AchievementType(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=100, unique=True)


class Achievement(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE,
                               primary_key=True)
    achievement_type = models.ForeignKey(AchievementType, on_delete=models.CASCADE,
                                         primary_key=True)
    value = models.FloatField()


class Expansion(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='expansions',
                              default='expansions/default.png')
    codename = models.CharField(max_length=100, unique=True)


class Card(models.Model):
    expansion = models.ForeignKey(Expansion, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='cards',
                              default='cards/default.jpg')
    codename = models.CharField(max_length=100, unique=True)
