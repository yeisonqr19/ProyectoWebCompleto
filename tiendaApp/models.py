from django.db import models

# Create your models here.

class Categoria(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "categorias"
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoriaProducto = models.ManyToManyField(Categoria)
    stock = models.PositiveIntegerField(default=0)
    created = models.DateField(auto_now_add=True, auto_created=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        
    def __str__(self):
        return self.nombre
