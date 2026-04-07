from . models import Project
from rest_framework import serializers

from tasks.models import Task

# Serializers go here
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at']

class ProjectSerializer(serializers.ModelSerializer):
    
    # This magic line pulls in all tasks linked to this project
    # This 'tasks' variable must match the 'related_name' in your Task model
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at', 'tasks']
        read_only_fields = ['id', 'created_at']