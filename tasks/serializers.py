from .models import Task
from rest_framework import serializers

# Serializers go here

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task

        fields = ['id', 'title', 'description', 'status', 'created_at']

        read_only_fields = ['id', 'created_at']