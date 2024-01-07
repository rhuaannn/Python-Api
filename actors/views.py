from rest_framework import generics
from actors.models import Actors


class ActorCreateListview(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = None

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = None