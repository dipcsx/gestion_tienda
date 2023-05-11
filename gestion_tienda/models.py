from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class bl_user(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    rolUsuario=models.CharField(max_length=15,default='VENDEDOR')
    nroCelular=models.CharField(max_length=15, default='')
    fechaIngreso=models.DateField(default=date.today)

class bl_producto(models.Model):
    usuarioProducto = models.ForeignKey(User, on_delete=models.CASCADE)
    nombProducto = models.CharField(max_length=32,default='')
    codProducto = models.CharField(max_length=32,default='')
    precioCompra = models.FloatField(max_length=10, default='')
    precioVenta = models.FloatField(max_length=10, default='')
