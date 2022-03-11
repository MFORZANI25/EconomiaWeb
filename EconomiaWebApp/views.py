from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormularioContacto

# Create your views here.

def inicio (request):
    return render (request, "EconomiaWebApp/inicio.html")

def servicios (request):
    return render (request, "EconomiaWebApp/servicios.html")

def mensaje (request):
    formulario_contacto= FormularioContacto()
    
    if request.method=="POST":
        formulario_contacto= FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre= request.POST.get("nombre")
            email= request.POST.get("email")
            
            return redirect("/mensaje")
    else:
        print("No se ha posido enviar, prueba nuevamente")
    return render (request, "EconomiaWebApp/contacto.html", {"mi_formulario": formulario_contacto})

def acerca_de_mi (request):
    return render (request, "EconomiaWebApp/about.html")