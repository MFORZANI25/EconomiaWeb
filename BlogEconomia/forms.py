from django import forms
from django.contrib.auth.models import User

class FormularioCrearBlog(forms.Form):
    Titulo = forms.CharField(max_length=25)
    Subtitulo= forms.CharField(max_length=25)
    Contenido= forms.CharField(max_length=1000)
    fecha= forms.DateTimeField(auto_now_add=True)
    imagen= forms.ImageField(upload_to='blog', null=True, blank=True)
