from django.urls import path
from . views import TaskListCreateView, TaskListDetailsView

urlpatterns = [
    path('', TaskListCreateView.as_view()),
    path('<int:pk>/', TaskListDetailsView.as_view())
]