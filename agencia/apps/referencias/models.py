from django.db import models
from apps.viajeros.models import Viajero
from apps.viajes.models import Viaje

class Referencia (models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    direccion = models.CharField(max_length=100, verbose_name="Direccion")
    telefono = models.CharField(max_length=100, verbose_name="Telefono")
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    viajero = models.ForeignKey(Viajero, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = "Referencia"
        verbose_name_plural = "Referencias"