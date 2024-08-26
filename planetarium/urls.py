from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AstronomyShowViewSet

router = DefaultRouter()
router.register(r"astronomy-shows", AstronomyShowViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
