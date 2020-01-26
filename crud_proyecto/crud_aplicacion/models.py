from django.db import models

class Cliente(models.Model):
    id = models.AutoField (primary_key = True)
    nombre = models.CharField(max_length=400)
    apellido = models.CharField(max_length=400)
    cedula = models.IntegerField (unique = True)
    fechaNacimiento = models.CharField(max_length=10)
    Direccion = models.CharField(max_length= 800)
