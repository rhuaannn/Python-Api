import json
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre

@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name = data['name'])

        new_genre.save()
        
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name},
            status=201,
            )

        
@csrf_exempt
def genre_detail_view(request, pk):
 try:
        genre = Genre.objects.get(pk=pk)
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    #No Django, quando você usa objects.get() ou get_object_or_404() para recuperar um objeto do banco de dados
    # e não encontra um objeto correspondente, uma exceção chamada DoesNotExist é levantada. Essa exceção faz parte da estrutura do Django
    # para lidar com casos em que uma consulta esperava encontrar um objeto, mas não encontrou.
 except Genre.DoesNotExist:
        return JsonResponse({'error': 'Genre not found'}, status=404)