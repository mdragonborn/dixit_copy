from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class Player(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    # IDAvatar = models.ForeignKey('Avatar', on_delete=models.SET_NULL ,null=True) #TODO default
    ProfilePicture = models.ImageField(upload_to='files/profile_pictures/', default='files/profile_pictures/default.jpg')
    IsAdmin = models.BooleanField(default=False)
    IsVip = models.BooleanField(default=False)
    VipExpiry = models.DateField(null=True)

    def __str__(self):
        return self.User.first_name  #TODO ic'

    @staticmethod
    def create_user(username, firstname, lastname, email, password):
        if User.objects.filter(username=username, email=email).exists():
            return None
        else:
            newPlayer = Player(User=User.objects.create_user(username,email,password))
            newPlayer.User.first_name=firstname
            newPlayer.User.last_name=lastname
            Player.save(newPlayer)
            return newPlayer

    # @staticmethod
    # def create_admin():

    # get_absolute_url ?