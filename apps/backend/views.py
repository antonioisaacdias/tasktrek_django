from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Project, Task

@login_required(login_url='login')
def create_task_view(request):
    name = request.POST.get('name')
    date = request.POST.get('date')
    time = request.POST.get('time')
    comments = request.POST.get('comments')
    project_id = request.POST.get('project')
    
    if time == "":
        time = None
        
    if project_id != None:
        try:
            project = Project.objects.get(id=project_id, user=request.user)
        except Project.DoesNotExist:
            return HttpResponse('Projeto inválido', status=404)
        
    else:
        project = project_id
        
    Task.objects.create(
        name=name,
        comments=comments,
        expire_date=date,
        expire_time=time,
        project=project,
        user=request.user
    )
    
    return HttpResponse('Tarefa criada com sucesso!',status=201)

