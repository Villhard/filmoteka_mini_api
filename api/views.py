from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Film, Favorite
from api.permissions import IsAdminOrReadOnly
from api.serializers import FilmSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(
        detail=True,
        methods=["POST", "DELETE"],
        permission_classes=[IsAuthenticated],
    )
    def favorite(self, request, pk):
        film = self.get_object()
        user = request.user
        instance = Favorite.objects.filter(film=film, user=user).first()

        if request.method == "POST":
            return self._add_to_favorites(instance, film, user)
        return self._remove_from_favorites(instance)

    def _add_to_favorites(self, instance, film, user):
        if instance:
            return Response(
                {"detail": "Фильм уже добавлен в избранное"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Favorite.objects.create(film=film, user=user)
        serializer = FilmSerializer(film, context={"request": self.request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def _remove_from_favorites(self, instance):
        if not instance:
            return Response(
                {"detail": "Фильм не найден в избранном"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_favorite_films(request):
    user = request.user
    favorite_films = Film.objects.filter(favorited_by__user=user)
    serializer = FilmSerializer(favorite_films, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)
