from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.

def contacto(request):
    
    contacto_form = ContactoForm()
    
    ctx = {
        'contacto_form':contacto_form,
    }
    
    return render(request, "contactoApp/contacto.html", ctx)

