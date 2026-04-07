from django.db import models
from django.contrib.auth.models import User

from projects.models import Project


# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done')
    ]


    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='TODO')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
