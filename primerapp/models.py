from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=50)
    pais = models.TextField()
    
class Item(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    costo_mensual = models.IntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.TextField()
    edad = models.IntegerField()
    password = models.CharField(max_length=15)