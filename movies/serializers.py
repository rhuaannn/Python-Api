from rest_framework import serializers
from movies.models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year <= 1990:
            raise serializers.ValidationError('Data inferior a 1990 não é permitido.')
        return value