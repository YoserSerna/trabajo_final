from django.urls import path, include
from apps.origenes.views import index,origenCreate,origenEdit,origenDelete
app_name = "origenes"; 

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', origenCreate, name='origenCreate'),
    path('actualizar/<int:id_origen>/', origenEdit, name='origenEdit'),
    path('eliminar/<int:id_origen>/', origenDelete, name='origenDelete'),
]