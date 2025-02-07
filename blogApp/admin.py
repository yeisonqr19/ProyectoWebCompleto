from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class Post_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Categoria, CategoriaAdmin)    
admin.site.register(Post, Post_Admin)

