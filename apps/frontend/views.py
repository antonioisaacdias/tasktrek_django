from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from ..backend.models import Project

from django.utils.timezone import now
from .forms import LoginForm

# Create your views here.
def login_view(request):
    timestamp = now().timestamp()
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')
    
    return render(request, 'frontend/login.html', {'timestamp': timestamp , 'form': form})

@login_required(login_url='login')
def home_view(request):
    timestamp = now().timestamp()
    projects = Project.objects.filter(user=request.user, is_active=True).order_by('name')
    projects_list = []
    
    for project in projects:
        projects_list.append({
            'id': project.id,
            'name': project.name,
            'color': project.color,
        })
    
    return render(request, 'frontend/home.html', {'timestamp': timestamp, 'projects': projects_list})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


