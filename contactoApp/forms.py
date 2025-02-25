from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Tu nombre', max_length=100, required=True)
    email = forms.EmailField(label='Tu Correo', required=True)
    contenido = forms.CharField(label='Mensaje', widget= forms.Textarea)
    

