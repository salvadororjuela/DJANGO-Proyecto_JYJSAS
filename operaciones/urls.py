from django.urls import path
from . import views


# Namespace para evitar conflicto entre urls llamadas igual pero en diferentes
# aplicaciones
app_name = "operaciones"

urlpatterns = [
    # Pagina comun al gerente, director operativo y almacenista
    path("", views.index, name="reportesinventario"),
    # Paginas comunes al gerente y almacenista
    path("nuevomaterial.html", views.nuevomaterial, name="nuevomaterial"),
    path("nuevoproveedor", views.nuevoproveedor, name="nuevoproveedor"),
    # Paginas comunes al gerente y director operativo
    path("nuevoproyecto", views.nuevoproyecto, name="nuevoproyecto"),
    # Paginas exclusivas del gerente
    path("nuevoempleado", views.nuevoempleado, name="nuevoempleado"),
    path("autsalidamaterial", views.autsalidamaterial,
         name="autsalidamaterial"),
    path("eliminarcontratista", views.eliminarcontratista,
         name="eliminarcontratista"),
    path("eliminarproducto", views.eliminarproducto, name="eliminarproducto"),
    path("eliminarproveedor", views.eliminarproveedor,
         name="eliminarproveedor"),
]
