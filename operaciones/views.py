from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Se importa para ejecutar los formularios en las paginas que los requieren
from django.contrib.auth import forms
# Se importa para cuando se envia la informacion desde el formulario, la
# guarde en la base de datos
from .models import Materia_prima, Movimientos_Almacen, Proveedores
from .models import Proyectos, Contratistas
from . import forms


""" ################## INICIO FUNCIONES PROPIAS DEL GERENTE ################"""


# Funcion para acceder a la pagina de reportes gerente
@login_required(login_url="/inventarios/ingresar")
def index(request):
    return render(request, "operaciones/reportesinventario.html")


# Funcion para acceder a la pagina de ingreso de materias primas al sistema
# gerente
@login_required(login_url="/inventarios/ingresar")
def nuevomaterial(request):
    if request.method == "POST":
        pass
    else:
        formulario = forms.NuevoProducto
        return render(request, "operaciones/nuevomaterial.html", {
            'formulario': formulario
        })


# Funcion para ingresar nuevos proveedores gerente
@login_required(login_url="/inventarios/ingresar")
def nuevoproveedor(request):
    if request.method == "POST":
        # Crea el formulario y obtiene la informacion introducida para guardar
        # en base de datos
        formulario = forms.NuevoProveedor(request.POST)
        # Si el formulario es correcto, guarda el nuevo proveedor
        if formulario.is_valid():
            formulario.save()
            return render(request, "inventarios/gerente.html", {
                "mensaje": "Proveedor Guardado Exitosamente!"
            })
        else:
            formulario = forms.NuevoProveedor
            return render(request, "operaciones/nuevoproveedor.html", {
                "formulario": formulario,
                'mensaje': "El proveedor ya existe. Cambie los datos."
            })
    else:
        formulario = forms.NuevoProveedor
        return render(request, "operaciones/nuevoproveedor.html", {
            "formulario": formulario
        })


# Funcion para ingresar nuevos proyectos gerente
@login_required(login_url="/inventarios/ingresar")
def nuevoproyecto(request):
    if request.method == "POST":
        # Crea el formulario y obtiene la informacion introducida para guardar
        # en base de datos
        formulario = forms.NuevoProyecto(request.POST)
        # Si el formulario es correcto, guarda el nuevo proveedor
        if formulario.is_valid():
            formulario.save()
            return render(request, "inventarios/gerente.html", {
                "mensaje": "Nuevo Proyecto Creado Exitosamente!"
            })
        else:
            formulario = forms.NuevoProyecto
            return render(request, "operaciones/nuevoproyecto.html", {
                "formulario": formulario,
                'mensaje': "Este Proyecto ya Existe. Verifique los Datos Ingresados."
            })
    else:
        formulario = forms.NuevoProyecto
        return render(request, "operaciones/nuevoproyecto.html", {
            'formulario': formulario
        })


# Funcion para ingresar nuevos empleados gerente
@login_required(login_url="/inventarios/ingresar")
def nuevoempleado(request):
    return render(request, "operaciones/nuevoempleado.html")


# Funcion para autorizar la salida de material gerente
@login_required(login_url="/inventarios/ingresar")
def autsalidamaterial(request):
    return render(request, "operaciones/autsalidamaterial.html")


# Funcion para mostrar el listado de contratistas que gerente puede editar
# o borrar
@login_required(login_url="/inventarios/ingresar")
def eliminarcontratista(request):
    listado = Contratistas.objects.all()
    return render(request, "operaciones/eliminarcontratista.html", {
        'listado': listado
    })


# Funcion para redirigir a la pagina de borrado de un determinado contratista
@login_required(login_url="/inventarios/ingresar")
# Recibe codigo_contratista como argumento para redireccionar a la pagina de un
# determinado contratista
def borrarcontratista(request, codigo_contratista):
    contratista = Contratistas.objects.get(
        codigo_contratista=codigo_contratista)
    if request.method == "POST":
        contratista.delete()
        return render(request, "inventarios/gerente.html", {
            'mensaje': "Producto Contrasta se ha Eliminado de Base de Datos!"
        })
    else:
        return render(request, "operaciones/borrarcontratista.html", {
            'contratista': contratista
        })


# Funcion para mostrar el listado de productos que el gerente puede editar
# o borrar
@login_required(login_url="/inventarios/ingresar")
def eliminarproducto(request):
    listado = Materia_prima.objects.all()
    return render(request, "operaciones/eliminarproducto.html", {
        'listado': listado
    })


# Funcion para redirigir a la pagina de borrado de un determinado producto
@login_required(login_url="/inventarios/ingresar")
# Recibe codigo_producto como argumento para redireccionar a la pagina de un
# determinado producto
def borrarproducto(request, codigo_producto):
    producto = Materia_prima.objects.get(codigo_producto=codigo_producto)
    if request.method == "POST":
        producto.delete()
        return render(request, "inventarios/gerente.html", {
            'mensaje': "Producto Borrado de la Base de Datos de Almacén!"
        })
    else:
        return render(request, "operaciones/borrarproducto.html", {
            'producto': producto
        })


# Funcion para mostrar el listado de proveedores que el gerente puede editar
# o borrar
@login_required(login_url="/inventarios/ingresar")
def eliminarproveedor(request):
    listado = Proveedores.objects.all()
    return render(request, "operaciones/eliminarproveedor.html", {
        'listado': listado
    })


# Funcion para redirigir a la pagina de borrado de un determinado proveedor
@login_required(login_url="/inventarios/ingresar")
# Recibe codigo_proveedor como argumento para redireccionar a la pagina de un
# determinado proveedor
def borrarproveedor(request, codigo_proveedor):
    proveedor = Proveedores.objects.get(codigo_proveedor=codigo_proveedor)
    if request.method == "POST":
        proveedor.delete()
        return render(request, "inventarios/gerente.html", {
            'mensaje': "Proveedor Eliminado de la Base de Datos!"
        })
    else:
        return render(request, "operaciones/borrarproveedor.html", {
            'proveedor': proveedor
        })


# Funcion para mostrar el listado de proyectos que el gerente puede editar
# o borrar
@login_required(login_url="/inventarios/ingresar")
def eliminarproyecto(request):
    listado = Proyectos.objects.all()
    return render(request, "operaciones/eliminarproyecto.html", {
        'listado': listado
    })


# Funcion para redirigir a la pagina de borrado de un determinado proveedor
@login_required(login_url="/inventarios/ingresar")
# Recibe codigo_proyecto como argumento para redireccionar a la pagina de un
# determinado proyecto
def borrarproyecto(request, codigo_proyecto):
    proyecto = Proyectos.objects.get(codigo_proyecto=codigo_proyecto)
    if request.method == "POST":
        proyecto.delete()
        return render(request, "inventarios/gerente.html", {
            'mensaje': "Proyecto Eliminado de la Base de Datos!"
        })
    else:
        return render(request, "operaciones/borrarproyecto.html", {
            'proyecto': proyecto
        })


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


# Funcion para ingresar nuevos proveedores almacenista
@login_required(login_url="/inventarios/ingresar")
def almacenistanuevoproveedor(request):
    if request.method == "POST":
        pass
    else:
        formulario = forms.NuevoProveedor
        return render(request, "operaciones/almacenistanuevoproveedor.html", {
            "formulario": formulario
        })


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
    if request.method == "POST":
        # Crea el formulario y obtiene la informacion introducida para guardar
        # en base de datos
        formulario = forms.NuevoProyecto(request.POST)
        # Si el formulario es correcto, guarda el nuevo proveedor
        if formulario.is_valid():
            formulario.save()
            return render(request, "inventarios/directoroperativo.html", {
                "mensaje": "Nuevo Proyecto Creado Exitosamente!"
            })
    else:
        formulario = forms.NuevoProyecto
        return render(request, "operaciones/operativonuevoproyecto.html", {
            'formulario': formulario
        })


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
