from django.shortcuts import render
from serviciosApp.models import Servicio

# Create your views here.
def servicios(request):
    
    servicios = Servicio.objects.all()
    
    ctx = {
        'servicios' : servicios
    }
    
    return render(request, "serviciosApp/servicios.html", ctx)
    