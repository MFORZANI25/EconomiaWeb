from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render

from CuentasApp.models import Avatar
from .forms import UserEditerForm, UserRegisterForm
from django.contrib.auth.models import User
import django
from django.contrib.auth.decorators import login_required


def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.data.get('username')
            passwd = form.data.get('password')

            user = authenticate(username=usuario, password=passwd)

            if user:
                login(request, user)

                return redirect('Blog')
            else:
                return redirect('Login')

        else:
            return redirect('Login')
    
    form = AuthenticationForm()

    return render(request, 'CuentasApp/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        

        if form.is_valid():
            
            username = form.data['username']
            try:
                user_new= User.objects.get(username=username)
            except django.contrib.auth.models.User.DoesNotExist:
                user_new= None
            if not user_new:
                form.save()

            return redirect('Login')

    else:
        print('asdfasdfadsf')        
        # form = UserCreationForm()
        form = UserRegisterForm(request.POST)

    return render(request, 'CuentasApp/register.html', {'form': form})


@login_required
def Perfil(request):
    usuario= request.user
    
    if request.method == 'POST':
        form = UserEditerForm(request.POST)
    
        if form.is_valid():
            informacion= form.cleaned_data
            
            usuario.email= informacion['email']
            usuario.password1= informacion ['password1']
            usuario.password2= informacion ['password2']
            usuario.descripcion= informacion['descripcion']
            usuario.save

            return render (request, 'CuentasApp/login.html')
        
    else:
        form= UserEditerForm(initial={'email':usuario.email})
        
    return render(request, 'CuentasApp/perfil.html', {'form': form , 'usuario': usuario})
