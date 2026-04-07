from django.contrib import admin
from .models import Project
from tasks.models import Task # Import Task from your other app

# 1. Define how Tasks should look inside the Project page
class TaskInline(admin.TabularInline):
    model = Task
    extra = 1 # Shows 1 empty row to add a new task immediately

# 2. Register Project with the Inline
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    list_display = ['name', 'user', 'created_at'] # Shows these columns in the main table
