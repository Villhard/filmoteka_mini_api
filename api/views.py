from rest_framework import viewsets

from api.models import Film
from api.serializers import FilmSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer