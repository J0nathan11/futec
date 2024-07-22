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

def listadoProducto(request):
    productos=Producto.objects.all()
    return render(request,'listadoProducto.html',{'productos':productos})
#nuevo
def nuevoProducto(request):
    return render(request, 'nuevoProducto.html')
#Guardar
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
#eliminar
def eliminarProducto(request,id):
    productoEliminar = Producto.objects.get(id=id)
    productoEliminar.delete()
    messages.success(request, 'Producto eliminado con éxito')
    return redirect('listadoProducto')
#editar
def editarProducto(request,id):
    productoEditar = Producto.objects.get(id=id)
    return render(request, 'editarProducto.html', {'productoEditar':productoEditar})
#Actualizar
def procesarActualizacionProducto(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    precio=request.POST['precio']
    stock=request.POST['stock']
    estado=request.POST['estado']
    foto=request.FILES.get("foto")
    productoConsultado=Producto.objects.get(id=id)
    productoConsultado.nombre=nombre
    productoConsultado.descripcion=descripcion
    productoConsultado.precio=precio
    productoConsultado.stock=stock
    productoConsultado.estado=estado
    productoConsultado.foto=foto
    productoConsultado.save()
    messages.success(request, 'Producto actualizado con éxito')
    return redirect('listadoProducto')