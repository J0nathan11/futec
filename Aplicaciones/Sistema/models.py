from django.db import models
from django.conf import settings
# Cargando modelo Producto
class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=500) 
    precio=models.CharField(max_length=50)
    stock=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    foto=models.FileField(upload_to='productos',null=True, blank=True)
    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4} - {5} "
        return fila.format(self.id,self.nombre,self.descripcion,self.precio,self.stock,self.estado)
    
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Producto, through='CartItem')

    def get_total_price(self):
        total = sum(item.producto.get_precio() * item.cantidad for item in self.cartitem_set.all())
        return total

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.producto.get_precio() * self.cantidad

# Añade un método para convertir el precio a decimal en el modelo Producto
def get_precio(self):
    return float(self.precio)

# Cargando modelo Cliente
class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    ci=models.CharField(max_length=15)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    correo=models.CharField(max_length=100, default='')
    telefono=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    foto=models.FileField(upload_to='clientes',null=True, blank=True)
    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4} - {5} - {6} "
        return fila.format(self.id,self.ci,self.nombre,self.apellido,self.telefono,self.direccion,self.descripcion)
    
#Cargando modelo Cotizacion
class Cotizacion(models.Model):
    id=models.AutoField(primary_key=True)
    ci_cli=models.CharField(max_length=15)
    nombre_apellido=models.CharField(max_length=50)
    correo=models.CharField(max_length=100)
    telefono=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=100)
    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4} - {5}"
        return fila.format(self.id,self.ci_cli,self.nombre_apellido,self.correo,self.telefono,self.descripcion)

