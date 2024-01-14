from rest_framework  import generics
from movies.models import Movies
from movies.serializers import MoviesModelSerializer, MoviesGetSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesModelSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
   
            return MoviesGetSerializer
        return MoviesModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class =  MoviesModelSerializer
    