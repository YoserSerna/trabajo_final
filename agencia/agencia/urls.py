"""agencia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.destinos.views import home
from apps.origenes.views import home
from apps.referencias.views import home
from apps.viajeros.views import home
from apps.viajes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('destinos/', include('apps.destinos.urls', namespace="destinos")),
    path('origenes/', include('apps.origenes.urls', namespace="origenes")),
    path('referencias/', include('apps.referencias.urls', namespace="referencias")),
    path('viajes/', include('apps.viajes.urls', namespace="viajes")),
    path('viajeros/', include('apps.viajeros.urls', namespace="viajeros")),
]
