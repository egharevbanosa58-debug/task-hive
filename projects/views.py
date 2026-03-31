from django.shortcuts import render

from .serializers import ProjectSerializer
from .models import Project

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProjectViewSet(ModelViewSet):
    # Lets not forget the good ól ingredients
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    # The Prvacy guard
    def get_queryset(self):
        projects = Project.objects.filter(user=self.request.user) # You could just return this right away
        return projects
    
    # The Automatic Tagging function
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    