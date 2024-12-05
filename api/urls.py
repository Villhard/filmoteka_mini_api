from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import FilmViewSet, get_favorite_films

router_v1 = DefaultRouter()
router_v1.register(r"films", FilmViewSet)

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/favorites/", get_favorite_films),
]
