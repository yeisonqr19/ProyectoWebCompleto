from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class VRegistro(View):
    
    def get(self, request):
        
        form = UserCreationForm()
        
        ctx = {
            'form': form,
        }
        
        return render(request, "registro/registro.html", ctx)
    
    def post(self, request):
        pass
    
