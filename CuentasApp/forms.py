from dataclasses import fields
import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username= forms.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'email',)

class UserEditerForm(UserCreationForm):
    email= forms.EmailField(label='Modificar Email')
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    descripcion=forms.CharField(max_length=25)
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'descripcion',)