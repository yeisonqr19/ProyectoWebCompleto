from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.

def contacto(request):
    
    contacto_form = ContactoForm()
    
    if request.method == "POST":
        #Esto lo que hace es que carga la informacion que el usuario esta enviando por POST en el formulario
        contacto_form = ContactoForm(data=request.POST)
        
        #Luego valido que el formulario que esta enviando el cliente este completamente lleno y que la informacion sea valida asi: 
        if contacto_form.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            
                
    ctx = {
        'contacto_form':contacto_form,
    }
    
    return render(request, "contactoApp/contacto.html", ctx)
