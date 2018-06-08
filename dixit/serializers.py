from rest_framework import serializers

import dixit.models as models


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Card
        fields = ('id', 'image', 'codename')


class AvatarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Avatar
        fields = ('image', 'codename')  # TODO: Does this need id?
