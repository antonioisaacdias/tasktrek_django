from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from dateutil.relativedelta import relativedelta
from calendar import monthrange
import datetime
import locale

from django.utils.timezone import now
from .forms import LoginForm

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

@login_required(login_url='login')
def create_task_modal_view(request):
    timestamp = now().timestamp()
    return render(request, 'frontend/partials/modals/create-task-modal.html', {'timestamp': timestamp, 'modal_title': 'Nova tarefa'})

@login_required(login_url='login')
def calendar_widget_view(request, year=None, month=None):
    timestamp = now().timestamp()
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    today = datetime.date.today()
    year = year or today.year
    month = month or today.month
    month_name = datetime.date(year, month, 1).strftime('%B').capitalize()
    week_first_day, total_days = monthrange(year, month)
    days = list(range(1, total_days + 1))
    current_month = datetime.date(year, month, 1)

    last_month = current_month - relativedelta(months=1)
    next_month = current_month + relativedelta(months=+1)
    
    context = {
        'year': year,
        'month': month,
        'month_name': month_name,
        'last_month': {'year': last_month.year, 'month': last_month.month},
        'next_month': {'year': next_month.year, 'month': next_month.month},
        'days': days,
        'start': week_first_day + 1,
    }

    return render(request, 'frontend/widgets/small-calendar.html',{'timestamp': timestamp, 'context': context})