from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Anime
from .serializers import AnimeSerializer

@api_view(['GET', 'POST'])
def anime_list(request):
    if request.method == 'GET':
        animes = Anime.objects.all()
        serializer = AnimeSerializer(animes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
