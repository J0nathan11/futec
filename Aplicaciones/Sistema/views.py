from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Cliente
from django.contrib import messages 
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

#----------------------------PRODUCTO----------------------------------------------------------
def producto(request):
    productos=Producto.objects.all()
    return render(request, 'producto.html',{'productos':productos})

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
    if request.method == 'POST':
        id = request.POST['id']
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']
        estado = request.POST['estado']
        nueva_foto = request.FILES.get("foto")
        # Obtener el producto existente
        productoConsultado = get_object_or_404(Producto, id=id)
        # Actualizar campos
        productoConsultado.nombre = nombre
        productoConsultado.descripcion = descripcion
        productoConsultado.precio = precio
        productoConsultado.stock = stock
        productoConsultado.estado = estado
        # Solo actualizar la foto si se proporciona una nueva
        if nueva_foto:
            productoConsultado.foto = nueva_foto
        # Guardar cambios
        productoConsultado.save()
        messages.success(request, 'Producto actualizado con éxito')
        return redirect('listadoProducto')
    else:
        return redirect('listadoProducto')

#----------------------------CLIENTE----------------------------------------------------------
def cliente(request):
    return render(request, 'cliente.html')

def listadoCliente(request):
    clientes=Cliente.objects.all()
    return render(request,'listadoCliente.html',{'clientes':clientes})
#nuevo
def nuevoCliente(request):
    return render(request, 'nuevoCliente.html')
#Guardar
def guardarCliente(request):
    ced=request.POST['ci']
    nom=request.POST['nombre']
    ape=request.POST['apellido']
    tel=request.POST['telefono']
    dir=request.POST['direccion']
    desc=request.POST['descripcion']
    fot=request.FILES.get("foto")
    nuevoCliente=Cliente.objects.create(ci=ced,nombre=nom,apellido=ape,telefono=tel,direccion=dir,descripcion=desc,foto=fot)
    messages.success(request, 'Cliente guardado con éxito')
    return redirect('listadoCliente')
#eliminar
def eliminarCliente(request,id):
    clienteEliminar = Cliente.objects.get(id=id)
    clienteEliminar.delete()
    messages.success(request, 'Cliente eliminado con éxito')
    return redirect('listadoCliente')
#editar
def editarCliente(request,id):
    clienteEditar = Cliente.objects.get(id=id)
    return render(request, 'editarCliente.html', {'clienteEditar':clienteEditar})
#Actualizar
def procesarActualizacionCliente(request):
    id=request.POST['id']
    ci=request.POST['ci']
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    telefono=request.POST['telefono']
    direccion=request.POST['direccion']
    descripcion=request.POST['descripcion']
    foto=request.FILES.get("foto")
    clienteConsultado=Cliente.objects.get(id=id)
    clienteConsultado.ci=ci
    clienteConsultado.nombre=nombre
    clienteConsultado.apellido=apellido
    clienteConsultado.telefono=telefono
    clienteConsultado.direccion=direccion
    clienteConsultado.descripcion=descripcion
    clienteConsultado.foto=foto
    clienteConsultado.save()
    messages.success(request, 'Cliente actualizado con éxito')
    return redirect('listadoCliente')