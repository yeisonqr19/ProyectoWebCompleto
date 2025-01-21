from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    
    return render(request, "proyectoWebApp/home.html")

def servicios(request):
    
    return HttpResponse("Pagina Servicios")

def tienda(request):
    
    return HttpResponse("Pagina Tienda")

def blog(request):
    
    return HttpResponse("Pagina blog")

def contacto(request):
    
    return HttpResponse("Pagina contacto")

