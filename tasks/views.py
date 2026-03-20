from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    # The Ingredients
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # The privacy guard that only shows the tasks of the logged in user
        queryset = Task.objects.filter(user=self.request.user)

        # The status filter part
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status=status_param)

        return queryset
    
    # The automatic tagging function that automatically assigns the logged in user to the created task
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}