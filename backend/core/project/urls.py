from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, BlogViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="project")
router.register("blogs", ProjectViewSet, basename="blog")

urlpatterns = [
    path("", include(router.urls))
]