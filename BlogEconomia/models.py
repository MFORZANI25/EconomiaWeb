from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Categoría (models.Model):
    nombre= models.CharField(max_length=25)
    
    
    def __str__(self):
        return self.nombre

class Blog(models.Model):
    Titulo = models.CharField(max_length=25)
    Subtitulo= models.CharField(max_length=25)
    Contenido= RichTextUploadingField(blank= True)
    categoria= models.ManyToManyField (Categoría)
    imagen= models.ImageField(upload_to='blog', null=True, blank=True)
    fecha= models.DateTimeField(auto_now_add=True)
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Titulo
