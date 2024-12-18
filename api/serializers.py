from rest_framework import serializers

from api.models import Film


class FilmSerializer(serializers.ModelSerializer):
    is_favorited = serializers.SerializerMethodField()

    def get_is_favorited(self, obj):
        user = self.context["request"].user
        return not user.is_anonymous and obj.favorited_by.filter(user=user).exists()

    class Meta:
        model = Film
        fields = ["id", "title", "description", "release_date", "is_favorited"]
