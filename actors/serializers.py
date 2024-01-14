from rest_framework import serializers
from actors.models import Actors

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Actors
        fields = '__all__'

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ['name', 'id']