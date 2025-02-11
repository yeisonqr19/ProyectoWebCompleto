from django.shortcuts import render
from .models import Categoria, Post

# Create your views here.
def blog(request):

    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    
    ctx  = {
        'posts': posts,
        'categorias': categorias,
    }
    
    return render(request, "blogApp/blog.html", ctx)



