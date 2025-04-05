from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.create_task_view, name='create_task'),
]