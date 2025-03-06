from django.shortcuts import render
from .models import Categoria, Producto
from django.db.models import Q

# Create your views here.
def tienda(request):
    
    productos = Producto.objects.all()
    categorias = Categoria.objects.filter(padre__isnull=True)
    
    ctx = {
        'productos': productos,
        'categorias': categorias,
        'filtro': False,
    }
    
    return render(request,"tiendaApp/tienda.html", ctx)

def productos_categorias(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    subcategorias = categoria.subcategorias.all()
    
    productos = Producto.objects.filter(
        Q(categorias=categoria) | Q(categorias__in=subcategorias))   
    
    ctx = {
        "productos": productos,
        "categorias":Categoria.objects.filter(padre__isnull=True),
        'filtro': True,
    }
    
    return render(request, "tiendaApp/tienda.html", ctx)

def productos_subcategorias(request, subcategoria_id):
    
    subcategoria = Categoria.objects.get(id =subcategoria_id)
    productos = Producto.objects.filter(categorias=subcategoria)
    
    ctx = {
        'productos': productos,
        'categorias': Categoria.objects.filter(padre__isnull=True),
        'filtro': True,
    }
    
    return render(request, "tiendaApp/tienda.html", ctx)