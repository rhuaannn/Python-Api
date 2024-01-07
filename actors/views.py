from rest_framework import generics
from actors.models import Actors
from actors.serializers import ActorSerializer

class ActorCreateListview(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer