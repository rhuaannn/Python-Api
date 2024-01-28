from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actors
from actors.serializers import ActorSerializer

class ActorCreateListview(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer