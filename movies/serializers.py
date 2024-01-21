from rest_framework import serializers
from movies.models import Movies

from actors.serializers import ActorGetNameSerializer



class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class MoviesGetSerializer(serializers.ModelSerializer):
    actors = ActorGetNameSerializer(many=True)
    class Meta:
        model = Movies
        fields = ['title','release_date','resume','actors']
        
    def validate_release_date(self, value):
        if value.year <= 1990:
            raise serializers.ValidationError('Data inferior a 1990 não é permitido.')
        return value