import dixit.models as models
from rest_framework import serializers

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Card
        fields = ('id', 'image', 'codename')

class AvatarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Avatar
        fields = ('image', 'codename')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Player
        fields = ('id','username','profile_picture')
