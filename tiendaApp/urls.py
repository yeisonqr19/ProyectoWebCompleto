from django.urls import path
from tiendaApp import views
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('', views.tienda, name="tienda"),
    
    path('categoria/<int:categoria_id>/', views.productos_categorias, name="productos_por_categoria"),
    
    path('subcategoria/<int:subcategoria_id>/', views.productos_subcategorias, name="productos_por_subcategoria")
]

