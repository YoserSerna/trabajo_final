from django.db import models
from django.shortcuts import render, redirect
from apps.viajeros.models import Viajero
from apps.viajeros.form import ViajeroForm


def index(request):
    viajero = Viajero.objects.all().order_by('-id')
    context = {'viajeros': viajero}
    return render(request, 'viajeros/index.html', context)

def home(request):
    return render(request, 'base/base.html')

def viajeroCreate(request):
    if(request.method == 'POST'):
        form = ViajeroForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('viajeros:index')
    else:
        form = ViajeroForm()
        return render(request, 'viajeros/formViajero.html',{'form': form})

def viajeroEdit(request, id_viajero):
    viajero = Viajero.objects.get(pk=id_viajero)
    
    if request.method == 'GET':
        form = ViajeroForm(instance=viajero)  
    else:
        form = ViajeroForm(request.POST, instance=viajero)
        if form.is_valid():
            form.save()
        return redirect('viajeros:index')
    return render(request, 'viajeros/formViajero.html', {'form': form})

def viajeroDelete(request, id_viajero):
    viajero = Viajero.objects.get(pk=id_viajero)
    if request.method == 'POST':
        viajero.delete()
        return redirect('viajeros:index')
    return render(request, 'viajeros/viajeroEliminar.html', {'viajeros': viajero})