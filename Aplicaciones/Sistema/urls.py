#Configurando el redireccionamiento

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('home/',views.home, name='home'),

    #----------------------------PRODUCTO-------------------------------------
    path('producto/', views.producto, name='producto'),
    path('listadoProducto/',views.listadoProducto, name="listadoProducto"),
    path('nuevoProducto/',views.nuevoProducto, name="nuevoProducto"),
    path('guardarProducto/',views.guardarProducto, name="guardarProducto"),
]
