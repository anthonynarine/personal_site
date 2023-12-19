from rest_framework import viewsets
from .models import Project, Blog
from .serializers import ProjectSerializer, BlogSerializer

class ProjectViewSet(viewsets.ModelViewset):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by("-posted_on")
    serializer_class = BlogSerializer
