from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('task/create', views.create_task_modal_view, name='create_task_modal'),
    path('task/update', views.update_task_modal_view,  name='update_task_modal'),
    path('calendar/', views.calendar_widget_view, name='calendar_widget'),
    path('calendar/<int:year>/<int:month>/', views.calendar_widget_view, name='calendar_widget_date'),
]