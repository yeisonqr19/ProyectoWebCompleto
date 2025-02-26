from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.

admin.site.site_header = "Panel de Administración"
admin.site.site_title = "Admin Tienda"
admin.site.index_title = "Gestión de la Tienda"

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "mostrar_categorias", "created")
    list_filter = ("categoriaProducto", "stock")
    search_fields = ("nombre", "descripcion")
    readonly_fields = ("created",)
    
    def mostrar_categorias(self, obj):
        return ", ".join([categoria.nombre for categoria in obj.categoriaProducto.all()])

    mostrar_categorias.short_description = "Categorías"
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
    