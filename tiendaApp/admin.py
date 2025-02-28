from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.

admin.site.site_header = "Panel de Administración"
admin.site.site_title = "Admin Tienda"
admin.site.index_title = "Gestión de la Tienda"

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "obtener_jerarquia")
    list_filter = ("padre",)
    search_fields = ("nombre",)
    readonly_fields = ("created", "updated")
    
    def obtener_jerarquia(self, obj):
        return obj.obtener_jerarquia()
    obtener_jerarquia.short_description = "Jerarquias"
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "mostrar_categorias", "created", "updated")
    list_filter = ("categorias", "stock")
    search_fields = ("nombre", "descripcion")
    readonly_fields = ("created", "updated")
    
    #Debo Crear esta funcion para poder mostrar Correctamente las categorias en el Panel Admin de mi Proyecto. 
    def mostrar_categorias(self, obj):
        return ", ".join([categoria.nombre for categoria in obj.categorias.all()])

    mostrar_categorias.short_description = "Categorías"
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)



