from django.contrib import admin
from django.urls import path
from todo_app.views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path("api/tasks/", TaskListCreateView.as_view()),
    path("api/tasks/<int:pk>/", TaskDetailView.as_view()),
]