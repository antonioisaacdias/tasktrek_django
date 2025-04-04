from django import forms
from ..backend.models import Task

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', max_length=150, widget=forms.TextInput(attrs={
        'class': 'input input-primary'
    }))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={
        'class': 'input input-primary'
    }))