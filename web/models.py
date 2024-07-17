# vehiculos/models.py
from django.db import models

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Foto(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, related_name='fotos', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='vehiculos/')
