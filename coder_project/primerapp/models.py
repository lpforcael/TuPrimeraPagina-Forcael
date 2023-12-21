from django.db import models


# Create your models here.

class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="ciudades", null=True, blank=True)
    
    def __str__(self):
        return self.nombre_ciudad +", "+ self.pais
    
class Item(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name="primerapp", null=True, blank=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=80)
    costo = models.IntegerField()
    #fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre +"; "+self.descripcion+" --> USD "+str(self.costo)+"; "+str(self.ciudad)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.TextField()
    edad = models.IntegerField()
    password = models.CharField(max_length=15)
    