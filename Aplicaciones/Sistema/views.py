from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages 
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

#----------------------------Producto----------------------------------------------------------
def producto(request):
    return render(request, 'producto.html')

def nuevoProducto(request):
    return render(request, 'nuevoProducto.html')

def guardarProducto(request):
    nom=request.POST['nombre']
    desc=request.POST['descripcion']
    prec=request.POST['precio']
    sto=request.POST['stock']
    est=request.POST['estado']
    fot=request.FILES.get("foto")
    nuevoProducto=Producto.objects.create(nombre=nom,descripcion=desc,precio=prec,stock=sto,estado=est,foto=fot)
    messages.success(request, 'Genero guardado con éxito')
    return redirect('listadoProducto')


def listadoProducto(request):
    productos=Producto.objects.all()
    return render(request,'listadoProducto.html',{'productos':productos})