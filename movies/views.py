from rest_framework  import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission
from movies.models import Movies
from movies.serializers import MoviesGetSerializer, MoviesSerializer
 
class MovieCreateListView(generics.ListCreateAPIView):
    
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MoviesGetSerializer
        return MoviesSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Movies.objects.all()
    serializer_class =  MoviesSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()

    def get(self, request):

        return response.Response(
            data = {'message': 'bateu aqui'},
            status = status.HTTP_200_OK,
        )