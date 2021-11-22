from django.db import models
from apps.viajeros.models import Viajero
from apps.viajes.models import Viaje

class Destino (models.Model):
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    viajero = models.ForeignKey(Viajero, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.viaje
    
    class Meta: 
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"