from django.urls import path, include
from apps.destinos.views import index,destinoCreate,destinoEdit,destinoDelete
app_name = "destinos"; 

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', destinoCreate, name='destinoCreate'),
    path('actualizar/<int:id_destino>/', destinoEdit, name='destinoEdit'),
    path('eliminar/<int:id_destino>/', destinoDelete, name='destinoDelete'),
]