from django.shortcuts import render
from .models import Categoria, Post

# Create your views here.
def blog(request):

    posts = Post.objects.all()
    
    ctx  = {
        'posts': posts,
    }
    
    return render(request, "blogApp/blog.html", ctx)



