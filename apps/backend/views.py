from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status
from .models import Project, Task
from django.db.models import Q
from datetime import datetime
from django.utils.timezone import now, localtime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task_view(request):
    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_active_projects_view(request):
    projects = Project.objects.filter(user=request.user, is_active=True).values('id', 'name', 'color').order_by('name')
    
    return Response(projects, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def list_tasks_view(request, date):
    if date == 'today':
        date = localtime(now()).date().isoformat()
        tasks = Task.objects.filter(
            Q(expire_date=date) | Q(expire_date__isnull=True),
            Q(project__is_active=True) | Q(project__isnull=True)
            ).values(
                'id',
                'name', 
                'comments', 
                'project__name', 
                'expire_date', 
                'expire_time', 
                'is_completed'
            ).order_by('expire_time')
    
        return Response({
                'date': date,
                'tasks': tasks
            }, status=status.HTTP_200_OK)
        
    tasks = Task.objects.filter(
        Q(expire_date=date) &
        (Q(project__is_active=True) | Q(project__isnull=True))
        ).values(
            'id',
            'name', 
            'comments', 
            'project__name', 
            'expire_date', 
            'expire_time', 
            'is_completed'
        ).order_by('expire_time')

    return Response({
            'date': date,
            'tasks': tasks
        }, status=status.HTTP_200_OK)
