from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
# Funcion para acceder a la pagina de reportes gerente
@login_required(login_url="/inventarios/ingresar")
def index(request):
    return render(request, "operaciones/reportesinventario.html")


""" ################## INICIO FUNCIONES PROPIAS DEL GERENTE ################"""


# Funcion para acceder a la pagina de ingreso de materias primas al sistema
# gerente
@login_required(login_url="/inventarios/ingresar")
def nuevomaterial(request):
    return render(request, "operaciones/nuevomaterial.html")


# Funcion para ingresar nuevos proveedores gerente
@login_required(login_url="/inventarios/ingresar")
def nuevoproveedor(request):
    return render(request, "operaciones/nuevoproveedor.html")


# Funcion para ingresar nuevos proyectos gerente
@login_required(login_url="/inventarios/ingresar")
def nuevoproyecto(request):
    return render(request, "operaciones/nuevoproyecto.html")


# Funcion para ingresar nuevos empleados gerente
@login_required(login_url="/inventarios/ingresar")
def nuevoempleado(request):
    return render(request, "operaciones/nuevoempleado.html")


# Funcion para autorizar la salida de material gerente
@login_required(login_url="/inventarios/ingresar")
def autsalidamaterial(request):
    return render(request, "operaciones/autsalidamaterial.html")


# Funcion para eliminar contratistas de la base de datos gerente
@login_required(login_url="/inventarios/ingresar")
def eliminarcontratista(request):
    return render(request, "operaciones/eliminarcontratista.html")


# Funcion para eliminar productos de la base de datos gerente
@login_required(login_url="/inventarios/ingresar")
def eliminarproducto(request):
    return render(request, "operaciones/eliminarproducto.html")


# Funcion para eliminar proveedores gerente
@login_required(login_url="/inventarios/ingresar")
def eliminarproveedor(request):
    return render(request, "operaciones/eliminarproveedor.html")


# Funcion para redireccionar al gerente al menu propio
@login_required(login_url="/inventarios/ingresar")
def redirecciongerente(request):
    return render(request, "inventarios/gerente.html")


""" ################ INICIO FUNCIONES PROPIAS DEL ALMACENISTA ##############"""


# Funcion para que el almacenista ingrese nuevo material a la base de datos
@login_required(login_url="/inventarios/ingresar")
def almacenistanuevomaterial(request):
    return render(request, "operaciones/almacenistanuevomaterial.html")


# Funcion para registrar salidas de material del almacen
@login_required(login_url="/inventarios/ingresar")
def salidaalmacen(request):
    return render(request, "operaciones/salidaalmacen.html")


# Funcion para solicitar autorizaciones de salida de materias de almacen
@login_required(login_url="/inventarios/ingresar")
def solautsalida(request):
    return render(request, "operaciones/solautsalida.html")


# Funcion para generar reportes al almacenista
@login_required(login_url="/inventarios/ingresar")
def almacenistareporteinventarios(request):
    return render(request, "operaciones/almacenistareporteinventarios.html")


# Funcion para redireccionar al almacenista al menu propio
@login_required(login_url="/inventarios/ingresar")
def redireccionalmacenista(request):
    return render(request, "inventarios/almacenista.html")


""" ########### INICIO FUNCIONES PROPIAS DEL DIRECTOR OPERACIONAL ##########"""


# Funcion del director operativo para solicitar materiales para obras
@login_required(login_url="solicitudmateriales")
def operativoreporteinventarios(request):
    return render(request, "operaciones/operativoreporteinventarios.html")


# Funcion del director operativo para solicitar materiales para obras
@login_required(login_url="solicitudmateriales")
def solicitudmateriales(request):
    return render(request, "operaciones/solicitudmateriales.html")


# Funcion del director operativo para solicitar materiales para obras
@login_required(login_url="solicitudmateriales")
def solicitudmateriales(request):
    return render(request, "operaciones/solicitudmateriales.html")


# Funcion para mostrar los proyectos a los que esta asignado un contratista
@login_required(login_url="/inventarios/ingresar")
def operativonuevoproyecto(request):
    return render(request, "operaciones/operativonuevoproyecto.html")


# Funcion para redireccionar al director operacional al menu propio
@login_required(login_url="/inventarios/ingresar")
def redireccionoperativo(request):
    return render(request, "inventarios/directoroperativo.html")


""" ############# INICIO FUNCIONES PROPIAS DE lOS CONTRATISTAS #############"""


# Funcion para mostrar los proyectos a los que esta asignado un contratista
@login_required(login_url="/inventarios/ingresar")
def proyectoscontratista(request):
    return render(request, "operaciones/proyectoscontratista.html")


# Funcion del contratista para reportar novedades
@login_required(login_url="/inventarios/ingresar")
def novedades(request):
    return render(request, "operaciones/novedades.html")


# Funcion para redireccionar al contratista al menu propio
@login_required(login_url="/inventarios/ingresar")
def redireccioncontratista(request):
    return render(request, "inventarios/contratista.html")
