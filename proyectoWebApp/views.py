from django.shortcuts import render, HttpResponse
from serviciosApp.models import Servicio

# Create your views here.

def home(request):
    
    return render(request, "proyectoWebApp/home.html")

