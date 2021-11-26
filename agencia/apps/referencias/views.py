from django.db import models
from django.shortcuts import render, redirect
from apps.referencias.models import Referencia
from apps.referencias.form import ReferenciaForm


def index(request):
    referencia = Referencia.objects.all().order_by('-id')
    context = {'referencias': referencia}
    return render(request, 'referencias/index.html', context)

def home(request):
    return render(request, 'base/base.html')

def referenciaCreate(request):
    if(request.method == 'POST'):
        form = ReferenciaForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('referencias:index')
    else:
        form = ReferenciaForm()
        return render(request, 'referencias/formReferencia.html',{'form': form})

def referenciaEdit(request, id_referencia):
    referencia = Referencia.objects.get(pk=id_referencia)
    
    if request.method == 'GET':
        form = ReferenciaForm(instance=referencia)  
    else:
        form = ReferenciaForm(request.POST, instance=referencia)
        if form.is_valid():
            form.save()
        return redirect('referencias:index')
    return render(request, 'referencias/formReferencia.html', {'form': form})

def referenciaDelete(request, id_referencia):
    referencia = Referencia.objects.get(pk=id_referencia)
    if request.method == 'POST':
        referencia.delete()
        return redirect('referencias:index')
    return render(request, 'referencias/referenciaEliminar.html', {'referencias': referencia})