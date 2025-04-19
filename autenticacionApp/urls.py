from django.urls import path
from .import views

app_name = "autenticacion"

urlpatterns = [
    path("", views.autenticacion, name="auth"),
    path("login/", views.login, name="login"),
]
