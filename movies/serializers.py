from rest_framework import serializers

 
from movies.models import Movies
 
from actors.serializers import ActorsSerializer
from genres.serializers import GenreSerializer


class MoviesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class MoviesGetSerializer(serializers.ModelSerializer):
    actors = ActorsSerializer(many=True)  # Usando o serializador ActorsSerializer para acessar o campo 'name'
    genre = GenreSerializer()
    
    class Meta:
        model = Movies
        fields = ['title', 'release_date', 'resume','genre','actors','genre']


        