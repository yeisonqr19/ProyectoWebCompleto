#Archivo Creado Por mi
from django.urls import path
from proyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('tienda/', views.tienda, name="tienda"),
    path('contacto/', views.contacto, name="contacto"),   
]

 #para que carguen correctamente las imagenes: 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



