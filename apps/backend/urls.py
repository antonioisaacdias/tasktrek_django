from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.new_task_view, name='new_task'),
]