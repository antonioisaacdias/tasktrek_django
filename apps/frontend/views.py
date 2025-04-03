from django.shortcuts import render
from django.utils.timezone import now
from .forms import LoginForm

# Create your views here.
def login_view(request):
    timestamp = now().timestamp()
    form = LoginForm(request.POST or None)
    return render(request, 'frontend/login.html', {'timestamp': timestamp , 'form': form})