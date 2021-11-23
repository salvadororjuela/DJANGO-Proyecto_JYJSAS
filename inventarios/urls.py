from django.urls import path
from . import views


# Namespace para evitar conflicto entre urls llamadas igual pero en diferentes
# aplicaciones
app_name = "inventarios"

urlpatterns = [
    # Camino a la pagina principal de la empresa
    path("", views.index, name="index"),
    path("mision", views.mision, name="mision"),
    path("vision", views.vision, name="vision"),
    path("contacto", views.contacto, name="contacto"),
    path("ingresar", views.ingresar, name="ingresar"),
    path("salir", views.salir_view, name="salir"),
    path("ingresoExitoso", views.ingresoExitoso, name="ingresoExitoso")
]
