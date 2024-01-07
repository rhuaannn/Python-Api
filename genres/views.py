from http.client import ResponseNotReady
from pstats import Stats
import statistics
from urllib import response
from django.http import JsonResponse
from rest_framework import generics
from genres.serializers import GenreSerializer
from genres.models import Genre

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

#########################################################
    # Lembrando que não é uma boa prática retornar corpo
    # em uma requisição de delete.
    # def delete(self, *args, **kwargs):
    #     instance = self.get_object()

    #     try:
    #         instance.delete()
    #         return JsonResponse({'message': 'Genre deletado com sucesso.'}, status=204)
    #     except Exception as e:
    #         return JsonResponse({'error': str(e)}, status=500)
        
 
 
        