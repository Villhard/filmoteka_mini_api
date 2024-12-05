from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    film = models.ForeignKey(
        Film, on_delete=models.CASCADE, related_name="favorited_by"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["film", "user"], name="unique_favorite")
        ]

    def __str__(self):
        return f"{self.user} - {self.film}"
