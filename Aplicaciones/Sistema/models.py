from django.db import models

# Cargando modelo
class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=500) 
    precio=models.CharField(max_length=50)
    stock=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    foto=models.FileField(upload_to='productos',null=True, blank=True)
    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4} "
        return fila.format(self.id,self.nombre,self.descripcion,self.precio,self.stock,self.estado)
