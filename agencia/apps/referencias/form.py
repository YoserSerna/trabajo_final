from django.forms import fields
from django import forms
from apps.referencias.models import Referencia
from django.forms import fields

class ReferenciaForm(forms.ModelForm):
    class Meta: 
        model = Referencia
        
        fields = [
            'nombre',
            'apellido',
            'direccion',
            'telefono',
            'viaje',
            'viajero'
        ]
        labels = {
            'nombre': 'Ingrese el Nombre',
            'apellido': 'Ingrese el Apellido',
            'direccion': 'Ingrese la Direccion',
            'telefono': 'Ingrese el telefono',
            'viaje': 'Seleccione el Viaje',
            'viajero': 'Seleccione el Viajero'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'viaje': forms.Select(attrs={'class': 'form-control'}),
            'viajero': forms.Select(attrs={'class': 'form-control'}),
        }