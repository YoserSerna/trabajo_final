from django.forms import fields
from django import forms
from apps.viajes.models import Viaje
from django.forms import fields

class ViajeForm(forms.ModelForm):
    class Meta: 
        model = Viaje
        
        fields = [
            'numero_plazas',
            'fecha_viaje',
            'viajero'
        ]
        labels = {
            'numero_plazas': 'Ingrese el Nombre',
            'fecha_viaje': 'Ingrese la Fecha',
            'viajero': 'Seleccione el Viajero'
        }
        widgets = {
            'numero_plazas': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_viaje': forms.DateInput(attrs={'class': 'form-control'}),
            'viajero': forms.Select(attrs={'class': 'form-control'}),
        }