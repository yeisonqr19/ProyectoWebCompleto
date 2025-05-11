from django.shortcuts import render, redirect
from .carritoApp import CarritoApp
from tiendaApp.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    
    carro = CarritoApp(request)
    
    producto = Producto.objects.get(id = producto_id)
    
    #Utilizo el Metodo de agregar Producto de la clase:
    carro.agregar_producto(producto = producto)
    
    return redirect("tienda:tienda")

def eliminar_producto(request, producto_id):
    
    carro = CarritoApp(request)
    
    producto = Producto.objects.get(id = producto_id)
    
    carro.eliminar_producto(producto = producto)
    
    return redirect("tienda:tienda")

def restar_producto(request, producto_id):
    
    carro = CarritoApp(request)
    
    producto = Producto.objects.get(id = producto_id)
    
    carro.restar_producto(producto = producto)
    
    return redirect("tienda:tienda")

def limpiar_carro(request):
    
    carro = CarritoApp(request)
    
    carro.limpiar_carro()    
    
    return redirect("tienda:tienda")
