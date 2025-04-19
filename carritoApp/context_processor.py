
def importe_total_carrito(request):
    total = 0
    
    #Valido si el usuario esta Autenticado en mi Aplicacion:
    
    #if request.session.is_authenticated:
    
    carro = request.session.get("carro", {})
    for key, value in carro.items():
       try:
           precio = float(value["precio"])
           cantidad = float(value["cantidad"])
           total += precio * cantidad
       except (ValueError, KeyError):
           continue
       
    return {"importe_total_carrito" : total}