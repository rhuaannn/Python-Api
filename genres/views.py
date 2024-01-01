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
        #'name' not in data: Esta parte verifica se a chave 'name' não está presente no dicionário data.
        # Se a chave não estiver presente, a condição é avaliada como True.
        # or: Este é um operador lógico que retorna True se pelo menos uma das condições for True.
        #   not data['name']: Esta parte verifica se o valor associado à chave 'name' em data é avaliado como falso.
        # Se o valor for vazio, nulo ou avaliado como falso, a condição é avaliada como True.
        #  Portanto, a linha completa if 'name' not in data or not data['name']: significa que a condição é True
        # se a chave 'name' não estiver presente em data ou se o valor associado a essa chave for vazio ou avaliado como falso.
        # Essa condição é usada para verificar se o campo 'name' está presente e não é vazio nos dados recebidos antes
        # de prosseguir com a criação de um novo objeto Genre. Se a condição for verdadeira, a resposta JSON com 
        # a mensagem de erro é retornada; caso contrário, o código continua com a criação do novo objeto Genre.
                
        if 'name' not in data or not data['name']:
            return JsonResponse({'Error': 'Nome é obrigatório!'}, status = 400)
        
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
        return JsonResponse({'error': 'Genero não encontrado!'}, status=404)