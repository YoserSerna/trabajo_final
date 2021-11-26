from django.urls import path, include
from apps.referencias.views import index,referenciaCreate,referenciaEdit,referenciaDelete
app_name = "referencias"; 

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', referenciaCreate, name='referenciaCreate'),
    path('actualizar/<int:id_referencia>/', referenciaEdit, name='referenciaEdit'),
    path('eliminar/<int:id_referencia>/', referenciaDelete, name='referenciaDelete'),
]