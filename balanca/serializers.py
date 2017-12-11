from django.contrib.auth.models import User, Group
from balanca.models import Pesagem
from rest_framework import serializers

class PesagemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pesagem
        fields = ('url','owner','peso','dataEHoraDePesagem',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    pesos = PesagemSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password','pesos')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


