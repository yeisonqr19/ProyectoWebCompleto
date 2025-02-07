from django.shortcuts import render
from .models import Categoria, Post

# Create your views here.
def blog(request):
    
    return render(request, "blogApp/blog.html")

