class CarritoApp:
    
    def __init__(self, request):
        
        #controlo la peticion que viene cuando creo una instancia de esta clase:
        self.request = request
        
        #Aqui estoy almacenando la sesion:s
        self.session = request.session
        
        #creo ahora un carro para esta sesion:
        carro = self.session.get("carro")
        
        #debo evaluar ahora, si el usuario esta ingresando por primera vez a ver el carro entonces se debe crear un carro nuevo, si hay algun elemento que ya tenga existente en el carro dentro de su sesion entonces debo cargar estos elementos:
        
        if not carro:
            carro = self.session['carro'] = {}
            
        self.carro = carro
        
    #voy a crear ahora esta funcion para agregar productos al carrito    
    def agregar_producto(self, producto):
        
        #Valido si Ya tengo ese producto en el carrito, ya que no puedo agregar repetidos:

        #Aqui estoy validando que el ID de los productos (que convierto a string) no este en el carro    
        if (str(producto.id) not in self.carro.keys()):
            
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad" : 1,
                "imagen": producto.imagen.url,
            }
        
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1 
                    break


        #Luego de editar el carrito, lo vuelvo a almacenar en la sesion:            
        self.guardar_carro()
    
                    
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
    
        
    def eliminar_producto(self, producto):
        
        producto.id = str(producto.id)
        
        #Verifico si el carrito tiene el producto buscado y elimina todas las unidades de este producto de inmediato.
        if producto.id in self.carro.keys():
            del self.carro[producto.id]
            self.guardar_carro()
    
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1 
                
                #Aqui valido, si hay menos de un elemento en el carrito entonces tiene es que eliminar el producto y no restarle 1. 
                if value["cantidad"] < 1 :
                    self.eliminar_producto(producto)    
                break    
            
        self.guardar_carro()
        
    def limpiar_carro(self):
        self.session["carro"] = {}
        #para editar nuevamente la sesion:
        self.session.modified = True