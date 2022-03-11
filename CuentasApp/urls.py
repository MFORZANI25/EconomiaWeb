from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LogoutView
from CuentasApp.views import *

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name= "CuentasApp/logout.html"), name= 'Logout'),
    path('signup', register, name="Register"),
    path('profile/', Perfil, name="Perfil"),
]

