from django.db import models
from django.shortcuts import render, redirect
from apps.destinos.models import Destino
from apps.destinos.form import DestinoForm


def index(request):
    destino = Destino.objects.all().order_by('-id')
    context = {'destinos': destino}
    return render(request, 'destinos/index.html', context)

def home(request):
    return render(request, 'base/base.html')

def destinoCreate(request):
    if(request.method == 'POST'):
        form = DestinoForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('destinos:index')
    else:
        form = DestinoForm()
        return render(request, 'destinos/formDestino.html',{'form': form})

def destinoEdit(request, id_destino):
    destino = Destino.objects.get(pk=id_destino)
    
    if request.method == 'GET':
        form = DestinoForm(instance=destino)  
    else:
        form = DestinoForm(request.POST, instance=destino)
        if form.is_valid():
            form.save()
        return redirect('destinos:index')
    return render(request, 'destinos/formDestino.html', {'form': form})

def destinoDelete(request, id_destino):
    destino = Destino.objects.get(pk=id_destino)
    if request.method == 'POST':
        destino.delete()
        return redirect('destinos:index')
    return render(request, 'destinos/destinoEliminar.html', {'destinos': destino})