from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class datosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipoUsuario=models.CharField(max_length=32, default='USUARIO')
    nroCelular=models.CharField(max_length=32, default='999905461')
    profesionUsuario=models.CharField(max_length=32, default='DEVELOPER')
    perfilUsuario=models.CharField(max_length=512, default='')
    fechaIngreso = models.DateField(default=date.today)
