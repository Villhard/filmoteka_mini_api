from rest_framework.serializers import ModelSerializer

from api.models import Film


class FilmSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = ["title", "description", "release_date"]
