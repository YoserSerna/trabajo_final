from django.urls import path, include
from apps.viajeros.views import index,viajeroCreate,viajeroEdit,viajeroDelete
app_name = "viajeros"; 

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', viajeroCreate, name='viajeroCreate'),
    path('actualizar/<int:id_viajero>/', viajeroEdit, name='viajeroEdit'),
    path('eliminar/<int:id_viajero>/', viajeroDelete, name='viajeroDelete'),
]