from django.urls import path
from .views import VRegistro

app_name = "autenticacion"

urlpatterns = [
    path("", VRegistro.as_view(), name="auth"),
]
