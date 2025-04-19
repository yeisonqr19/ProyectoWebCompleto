from django.shortcuts import render

# Create your views here.

def autenticacion (request):
    
    return render(request, "registro/registro.html")
    
def login(request):
    
    return render(request, "login/login.html")

