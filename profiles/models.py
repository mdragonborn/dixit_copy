from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class Player(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    # IDAvatar = models.ForeignKey('Avatar', on_delete=models.SET_NULL ,null=True) #TODO default
    # ProfilePicture = models.ImageField(upload_to='files/profile_pictures/',
    #                                   default='files/profile_pictures/default.jpg')
    IsAdmin = models.BooleanField(default=False)
    IsVip = models.BooleanField(default=False)
    VipExpiry = models.DateField(null=True)

    # on_delete = ?, on_update = ? or None?
    Avatar = models.ForeignKey(Avatar)

    def __str__(self):
        return self.User.first_name  # TODO ic'

    @staticmethod
    def create_user(username, firstname, lastname, email, password):
        if User.objects.filter(username=username, email=email).exists():
            return None
        else:
            newPlayer = Player(User=User.objects.create_user(username, email, password))
            newPlayer.User.first_name = firstname
            newPlayer.User.last_name = lastname
            Player.save(newPlayer)
            return newPlayer

    @staticmethod
    def does_user_exist(username, email):
        if User.objects.filter(username=username, email=email).exists():
            return None;
        return User.objects.filter(username=username, email=email)
        # @staticmethod
        # def create_admin():

        # get_absolute_url ?


class Avatar(models.Model):
    # nisam siguran gde ovaj upload_to treba da vodi. Stavio sam 'images/' kao naogvestaj
    Image = models.ImageField(upload_to='files/profile_pictures/',
                              default='files/profile_pictures/default.jpg', null=False)
    Codename = models.CharField(max_length=100, null=False, unique=True)


class Constant(models.Model):
    Name = models.CharField(max_length=255, null=False)
    Value = models.IntegerField()


class Color(models.Model):
    # on_delete = ?, on_update = ? or None?
    Constant = models.ForeignKey(Constant)


class Expansion(models.Model):
    Name = models.CharField(max_length=255, null=False)
    Image = models.ImageField(upload_to='files/expansion_pictures/',
                              default='files/expansion_pictures/default.jpg')
    Codename = models.CharField(max_length=100, null=False, unique=True)


class Card(models.Model):
    # on_delete = ?, on_update = ? or None?
    Expansion = models.ForeignKey(Expansion, null=False)
    Image = models.ImageField(upload_to='files/card_pictures/',
                              default='files/card_pictures/default.jpg')
    Codename = models.CharField(max_length=100, null=False, unique=True)
