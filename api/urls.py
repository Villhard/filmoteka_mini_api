from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import FilmViewSet

router_v1 = DefaultRouter()
router_v1.register(r"films", FilmViewSet)

urlpatterns = [
    path("api/v1/", include(router_v1.urls)),
]
