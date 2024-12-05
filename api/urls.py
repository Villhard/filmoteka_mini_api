from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import FilmViewSet, FavoriteFilmsView

router_v1 = DefaultRouter()
router_v1.register(r"films", FilmViewSet)

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/favorites/", FavoriteFilmsView.as_view()),
]
