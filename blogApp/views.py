from django.shortcuts import render
from .models import Categoria, Post

# Create your views here.
def blog(request):

    posts = Post.objects.all()
    
    ctx  = {
        'posts': posts,
    }
    
    return render(request, "blogApp/blog.html", ctx)

def categoria(request, categoria_id):
    
    categoria = Categoria.objects.get(id = categoria_id)
    posts = Post.objects.filter(categorias = categoria)
    
    ctx = {
        'categoria':categoria,
        'posts':posts,
    }
    
    return render(request, "blogApp/categorias.html", ctx)


