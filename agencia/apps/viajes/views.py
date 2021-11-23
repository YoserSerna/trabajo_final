from django.db import models
from django.shortcuts import render, redirect
from apps.viajes.models import Viaje
from apps.viajes.form import ViajeForm


def index(request):
    viaje = Viaje.objects.all().order_by('-id')
    context = {'viajes': viaje}
    return render(request, 'viajes/index.html', context)

def home(request):
    return render(request, 'base/base.html')

def viajeCreate(request):
    if(request.method == 'POST'):
        form = ViajeForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('viajes:index')
    else:
        form = ViajeForm()
        return render(request, 'viajes/formViaje.html',{'form': form})

def viajeEdit(request, id_viajero):
    viaje = Viaje.objects.get(pk=id_viaje)
    
    if request.method == 'GET':
        form = ViajeForm(instance=viaje)  
    else:
        form = ViajeForm(request.POST, instance=viaje)
        if form.is_valid():
            form.save()
        return redirect('viajes:index')
    return render(request, 'viajes/formViaje.html', {'form': form})

def viajeDelete(request, id_viaje):
    viaje = Viaje.objects.get(pk=id_viaje)
    if request.method == 'POST':
        viaje.delete()
        return redirect('viajes:index')
    return render(request, 'viajes/viajeEliminar.html', {'viajes': viaje})