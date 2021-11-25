from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
# Funcion para acceder a la pagina de reportes
@login_required(login_url="/inventarios/ingresar")
def index(request):
    return render(request, "operaciones/reportesinventario.html")


# Funcion para acceder a la pagina de ingreso de materias primas al sistema
@login_required(login_url="/inventarios/ingresar")
def nuevomaterial(request):
    return render(request, "operaciones/nuevomaterial.html")


# Funcion para ingresar nuevos proveedores
@login_required(login_url="/inventarios/ingresar")
def nuevoproveedor(request):
    return render(request, "operaciones/nuevoproveedor.html")


# Funcion para ingresar nuevos proyectos
@login_required(login_url="/inventarios/ingresar")
def nuevoproyecto(request):
    return render(request, "operaciones/nuevoproyecto.html")


# Funcion para ingresar nuevos empleados
@login_required(login_url="/inventarios/ingresar")
def nuevoempleado(request):
    return render(request, "operaciones/nuevoempleado.html")


# Funcion para autorizar la salida de material
@login_required(login_url="/inventarios/ingresar")
def autsalidamaterial(request):
    return render(request, "operaciones/autsalidamaterial.html")


# Funcion para eliminar contratistas de la base de datos
@login_required(login_url="/inventarios/ingresar")
def eliminarcontratista(request):
    return render(request, "operaciones/eliminarcontratista.html")


# Funcion para eliminar productos de la base de datos
@login_required(login_url="/inventarios/ingresar")
def eliminarproducto(request):
    return render(request, "operaciones/eliminarproducto.html")


# Funcion para eliminar proveedores
@login_required(login_url="/inventarios/ingresar")
def eliminarproveedor(request):
    return render(request, "operaciones/eliminarproveedor.html")
