from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Task
from .serializers import TaskSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TaskListCreateView(APIView):
    # We need this to be available to only authenticated users
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tasks = Task.objects.filter(user=request.user) # Ensures the current logged in user sees only their task
        serializer = TaskSerializer(tasks, many=True) # Ensures That not only onel task data comes out
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user) # Important because we want whatsoever task added is saved to the logged in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class TaskListDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    # To get the specific task shii
    def get_object(self, pk, user):
        try:
            return Task.objects.get(pk=pk, user=user)
        except Task.DoesNotExist:
            return None
        
    # The get method for the specific task
    def get(self, request, pk):
        task = Task.object.filter(user=request.user)

        status_param = request.query_params.get('status')

        if status_param:
            task = task.filter(status=status_param)

        serializer = TaskSerializer(task, many=True)

        return Response(serializer.data)
    
    # The Patch method for the specific task
    def patch(self, request, pk):
        task = self.get_object(pk, request.user)

        if not task:
            return Response({ 'error': 'Task Not Found' }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(task, data=request.data, partial=True)

        # Since we are patching...
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # The Delete method of the specific task
    def delete(self, pk, request):
        task = self.get_object(pk, request.user)

        if not task:
            return Response({ 'error': 'Task Not found' }, status=status.HTTP_400_BAD_REQUEST)
        task.delete()
        return Response({ 'message': 'Task Deleted Successfully' }, status=status.HTTP_204_NO_CONTENT)
            
