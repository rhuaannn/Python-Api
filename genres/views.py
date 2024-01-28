from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from genres.permissions import GenrePermissionClass
from genres.serializers import GenreSerializer
from genres.models import Genre

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GenrePermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

