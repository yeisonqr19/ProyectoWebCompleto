from django.shortcuts import render
from .models import Categoria, Producto


# Create your views here.
def tienda(request):
    
    productos = Producto.objects.all()
    
    nombre_productos = [producto.nombre for producto in productos]
    
    ctx = {
        'productos': productos,
    }
    
    return render(request,"tiendaApp/tienda.html", ctx)