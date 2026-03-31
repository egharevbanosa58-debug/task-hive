from .models import Task
from rest_framework import serializers

# Serializers go here

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task

        fields = ['id', 'title', 'description', 'status', 'project', 'created_at']

        read_only_fields = ['id', 'created_at']

    def validate_project(self, value):
        request = self.context.get('request') # Important

        # This is just to ensure that the project belongs to the user
        if value and value.user != request.user:
            raise serializers.ValidationError("You no fit use anoda man's Project")
        
        return value