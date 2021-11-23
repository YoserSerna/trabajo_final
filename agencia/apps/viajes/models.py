from django.db import models
from apps.viajeros.models import Viajero

class Viaje (models.Model):
    numero_plazas = models.CharField(max_length=100, verbose_name="Numero_plazas")
    fecha_viaje = models.DateField(verbose_name="Fecha")
    viajero = models.ForeignKey(Viajero, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.numero_plazas
    
    class Meta: 
        verbose_name = "Viaje"
        verbose_name_plural = "Viajes"