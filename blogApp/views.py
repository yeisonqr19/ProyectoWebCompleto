from django.shortcuts import render
from .models import Categoria, Post

#Para filtrar Los blogs por autores:
from django.contrib.auth.models import User

# Create your views here.
def blog(request):

    posts = Post.objects.all()
    
    categorias = set()
    
    for post in posts:
        for categoria in post.categorias.all():
            categorias.add(categoria)
    
    autores = set(post.autor for post in posts)
    #autores = {post.autor for post in posts}
    # Esto es una compresion De conjuntos, es como si hiciera:
    # Recorremos todos los posts y agregamos su autor al conjunto
    # autores = set()
    # for post in posts:
    #   autores.add(post.autor)
    
    ctx  = {
        'posts': posts,
        'categorias':categorias,
        'autores':autores,
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

def autor(request, autor_id):
    
    autor = User.objects.get(id = autor_id)
    posts = Post.objects.filter(autor = autor)
    
    ctx = {
        'autor':autor,
        'posts':posts,
    }
    
    return render(request, "blogApp/autores.html", ctx)