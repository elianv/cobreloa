from random import choices
from django.db import models
from pkg_resources import require

# Create your models here.

class Socio(models.Model):

    OCUPACION_CHOICES = [
        ('E', 'Estudiando'),
        ('J', 'Jubilado'),
        ('T', 'Trabajador'),
        ('O', 'Otra/No especifica')
    ]
    
    rut = models.CharField(unique=True, max_length=8, blank=False)
    dv = models.CharField(max_length=1, blank=False)
    correo = models.CharField(max_length=50, blank=False)
    nombres = models.CharField(max_length=50, blank=False)
    apellidos = models.CharField(max_length=50, blank=False)
    direccion = models.CharField(max_length=200, blank=False)
    telefono = models.CharField(max_length=9)
    foto = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    ocupacion = models.CharField(choices=OCUPACION_CHOICES, max_length=1)
    
