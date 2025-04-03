from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

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
    return render(request, 'frontend/home.html', {'timestamp': timestamp})    

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

