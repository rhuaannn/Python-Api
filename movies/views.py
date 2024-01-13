from rest_framework  import generics
from movies.models import Movies
from movies.serializers import MoviesSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class =  MoviesSerializer