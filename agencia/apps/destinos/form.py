from django.forms import fields
from django import forms
from apps.destinos.models import Destino
from django.forms import fields

class DestinoForm(forms.ModelForm):
    class Meta: 
        model = Destino
        
        fields = [
            'viaje',
            'viajero'
        ]
        labels = {
            'viaje': 'Seleccione el Viaje',
            'viajero': 'Seleccione el Viajero'
        }
        widgets = {
            'viaje': forms.Select(attrs={'class': 'form-control'}),
            'viajero': forms.Select(attrs={'class': 'form-control'}),
        }