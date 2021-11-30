from django.urls import path
from . import views


# Namespace para evitar conflicto entre urls llamadas igual pero en diferentes
# aplicaciones
app_name = "operaciones"

urlpatterns = [
    # Paginas gerente
    path("", views.index, name="reportesinventario"),
    path("nuevomaterial.html", views.nuevomaterial, name="nuevomaterial"),
    path("nuevoproveedor", views.nuevoproveedor, name="nuevoproveedor"),
    path("nuevoproyecto", views.nuevoproyecto, name="nuevoproyecto"),
    path("nuevoempleado", views.nuevoempleado, name="nuevoempleado"),
    path("autsalidamaterial", views.autsalidamaterial,
         name="autsalidamaterial"),
    path("eliminarcontratista", views.eliminarcontratista,
         name="eliminarcontratista"),
    path("eliminarproducto", views.eliminarproducto, name="eliminarproducto"),
    path("eliminarproveedor", views.eliminarproveedor,
         name="eliminarproveedor"),
    # Pagina borrado exclusiva de un proveedor
    path("<int:codigo_proveedor>", views.borrarproveedor,
         name="borrarproveedor"),

    path("redirecciongerente", views.redirecciongerente,
         name="redirecciongerente"),  # Redirecciona al menu del gerente

    # Paginas almacenista
    path("almacenistanuevomaterial", views.almacenistanuevomaterial,
         name="almacenistanuevomaterial"),
    path("salidaalmacen", views.salidaalmacen, name="salidaalmacen"),
    path("solautsalida", views.solautsalida, name="solautsalida"),
    path("almacenistareporteinventarios", views.almacenistareporteinventarios,
         name="almacenistareporteinventarios"),
    path("almacenistanuevoproveedor", views.almacenistanuevoproveedor,
         name="almacenistanuevoproveedor"),
    path("redireccionalmacenista", views.redireccionalmacenista,
         name="redireccionalmacenista"),  # Redirecciona al menu almacenista

    # Paginas director operativo
    path("operativoreporteinventarios", views.operativoreporteinventarios,
         name="operativoreporteinventarios"),
    path("solicitudmateriales", views.solicitudmateriales,
         name="solicitudmateriales"),
    path("operativonuevoproyecto", views.operativonuevoproyecto,
         name="operativonuevoproyecto"),
    path("redireccionoperativo", views.redireccionoperativo,
         name="redireccionoperativo"),  # Redirecciona al menu del operativo

    # Paginas contratistas
    path("proyectoscontratista", views.proyectoscontratista,
         name="proyectoscontratista"),
    path("novedades", views.novedades, name="novedades"),
    path("redireccioncontratista", views.redireccioncontratista,
         name="redireccioncontratista"),  # Redirecciona al menu contratistas
]
