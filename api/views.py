from rest_framework import viewsets

from api.models import Film
from api.serializers import FilmSerializer
from api.permissions import IsAdminOrReadOnly


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAdminOrReadOnly]
