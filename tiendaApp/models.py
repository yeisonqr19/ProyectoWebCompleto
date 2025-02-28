from django.db import models

# Create your models here.

class Categoria(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    
    #variable recursiva para que categoria pueda ser padre de otra categoria.
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="subcategorias")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
     
    class Meta:
        verbose_name = "Categoria" 
        verbose_name_plural = "categorias"
    
    def __str__(self):
        return self.nombre
    
    def obtener_jerarquia(self):
        
        if self.padre:
            return f"{self.padre.obtener_jerarquia()} > {self.nombre}"
        
        return self.nombre
    
class Producto(models.Model):
    
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="tienda/productos", null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categorias = models.ManyToManyField(Categoria)
    stock = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        
    def __str__(self):
        return self.nombre
