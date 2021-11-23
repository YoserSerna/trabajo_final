from django.urls import path, include
from apps.viajes.views import index,viajeCreate,viajeEdit,viajeDelete
app_name = "viajes"; 

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', viajeCreate, name='viajeCreate'),
    path('actualizar/<int:id_viaje>/', viajeEdit, name='viajeEdit'),
    path('eliminar/<int:id_viaje>/', viajeDelete, name='viajeDelete'),
]