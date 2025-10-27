from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cliente(models.Model): 

    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    identificacion = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Relación con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
