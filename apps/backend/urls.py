from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.create_task_view, name='create_task'),
    path('tasks/date/<str:date>/', views.list_tasks_view, name='list_tasks_date'),
    path('projects/active/', views.list_active_projects_view, name='list_active_projects')
]