from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='user', null=True, blank=True)
    Descripcion = models.CharField(max_length=25, null=True, blank=True)
    email= models.EmailField(max_length=50, null=True, blank=True)