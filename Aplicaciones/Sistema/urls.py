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
    path('eliminarProducto/<id>',views.eliminarProducto, name='eliminarProducto'),
    path('editarProducto/<id>',views.editarProducto, name="editarProducto"),
    path('procesarActualizacionProducto/',views.procesarActualizacionProducto, name="procesarActualizacionProducto"),
    #----------------------------CLIENTE--------------------------------------
    path('cliente/', views.cliente, name='cliente'),
    path('listadoCliente/',views.listadoCliente, name="listadoCliente"),
    path('nuevoCliente/',views.nuevoCliente, name="nuevoCliente"),
    path('guardarCliente/',views.guardarCliente, name="guardarCliente"),
    path('eliminarCliente/<id>',views.eliminarCliente, name='eliminarCliente'),
    path('editarCliente/<id>',views.editarCliente, name="editarCliente"),
    path('procesarActualizacionCliente/',views.procesarActualizacionCliente, name="procesarActualizacionCliente"),

    #----------------------------COTIZACION--------------------------------------
    path('cotizacion/', views.cotizacion, name='cotizacion'),
    path('listadoCotizacion/',views.listadoCotizacion, name="listadoCotizacion"),
    path('nuevaCotizacion/',views.nuevaCotizacion, name="nuevaCotizacion"),
    path('guardarCotizacion/',views.guardarCotizacion, name="guardarCotizacion"),
    path('eliminarCotizacion/<id>',views.eliminarCotizacion, name="eliminarCotizacion"),

    #-----------------------------CARRITO---------------------------
    path('agregarProductoCarrito/<int:product_id>/', views.agregarProductoCarrito, name='agregarProductoCarrito'),
    path('cart/', views.verCarrito, name='verCarrito'),
    path('eliminarProductoCarrito/<int:product_id>/', views.eliminarProductoCarrito, name='eliminarProductoCarrito'),
]
