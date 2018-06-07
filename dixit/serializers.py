import dixit.models as models
from rest_framework import serializers

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Card
        fields = ('id', 'expansion', 'image', 'codename')

class AvatarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Avatar
        fields = ('image', 'codename')

