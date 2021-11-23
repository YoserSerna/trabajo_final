from django.db import models


class Viajero (models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    direccion = models.CharField(max_length=100, verbose_name="Direccion")
    telefono = models.CharField(max_length=100, verbose_name="Telefono")
    
    
    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = "Viajero"
        verbose_name_plural = "Viajeros"