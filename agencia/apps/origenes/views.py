from django.db import models
from django.shortcuts import render, redirect
from apps.origenes.models import Origen
from apps.origenes.form import OrigenForm


def index(request):
    origen = Origen.objects.all().order_by('-id')
    context = {'origenes': origen}
    return render(request, 'origenes/index.html', context)

def home(request):
    return render(request, 'base/base.html')

def origenCreate(request):
    if(request.method == 'POST'):
        form = OrigenForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('origenes:index')
    else:
        form = OrigenForm()
        return render(request, 'origenes/formOrigen.html',{'form': form})

def origenEdit(request, id_origen):
    origen = Origen.objects.get(pk=id_origen)
    
    if request.method == 'GET':
        form = OrigenForm(instance=origen)  
    else:
        form = OrigenForm(request.POST, instance=origen)
        if form.is_valid():
            form.save()
        return redirect('origenes:index')
    return render(request, 'origenes/formOrigen.html', {'form': form})

def origenDelete(request, id_origen):
    origen = Origen.objects.get(pk=id_origen)
    if request.method == 'POST':
        origen.delete()
        return redirect('origenes:index')
    return render(request, 'origenes/origenEliminar.html', {'origenes': origen})