
def importe_total_carrito(request):
    total = 0
    
    #Valido si el usuario esta Autenticado en mi Aplicacion:
    if request.user.is_authenticated:
        for key, value in request.session["carro"]:
            total = total + float(value["precio"] * value["cantidad"])
            
    return {"importe_total_carrito" : total}