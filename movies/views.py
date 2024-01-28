from rest_framework  import generics
from rest_framework.permissions import IsAuthenticated
 
from movies.models import Movies
from movies.serializers import MoviesGetSerializer, MoviesSerializer
 
class MovieCreateListView(generics.ListCreateAPIView):
    
    permission_classes = (IsAuthenticated)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MoviesGetSerializer
        return MoviesSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class =  MoviesSerializer