from django.forms import fields
from django import forms
from apps.viajeros.models import Viajero
from django.forms import fields

class ViajeroForm(forms.ModelForm):
    class Meta: 
        model = Viajero
        
        fields = [
            'nombre',
            'direccion',
            'telefono'
        ]
        labels = {
            'nombre': 'Ingrese el Nombre',
            'direccion': 'Ingrese la Direccion',
            'telefono': 'Ingrese el telefono'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }