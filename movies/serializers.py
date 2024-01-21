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
        fields = ['title', 'release_date', 'resume','actors','genre']

    def validate_release_date(self, value):
        if value.year <= 1990:
            raise serializers.ValidationError('Data inferior a 1990 não é permitido.')
        return value
        