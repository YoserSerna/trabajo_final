from django.forms import fields
from django import forms
from apps.origenes.models import Origen
from django.forms import fields

class OrigenForm(forms.ModelForm):
    class Meta: 
        model = Origen
        
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