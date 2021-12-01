from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Se importa para ejecutar los formularios en las paginas que los requieren
from django.contrib.auth import forms
# Se importa para cuando se envia la informacion desde el formulario, la
# guarde en la base de datos
from .models import Materia_prima, Proveedores
from .models import Proyectos, Contratistas
from . import forms


""" ################## INICIO FUNCIONES PROPIAS DEL GERENTE ################"""


# Funcion para acceder a la pagina de reportes gerente
@login_required(login_url="/inventarios/ingresar")
def index(request):
    return render(request, "operaciones/reportesinventario.html")


# Funcion para acceder a la pagina de ingreso de materias primas al almacen
# gerente
@login_required(login_url="/inventarios/ingresar")
def entradaalmacen(request):
    if request.method == "POST":
        # Crea el formulario y obtiene la informacion introducida para guardar
        # en base de datos
        formulario = forms.Entrada_Almacen(request.POST)
        # Si el formulario es valido, guarda el nuevo producto
        if formulario.is_valid():
            formulario.save()
            return render(request, "inventarios/gerente.html", {
                "mensaje": "Entrada al Almacen Correcta!"
            })
        else:
            formulario = forms.Entrada_Almacen()
            return render(request, "operaciones/entradaalmacen.html", {
                'formulario': formulario,
                "mensaje": "Verifique los datos ingresados"
            })
    else:
        formulario = forms.Entrada_Almacen()
        return render(request, "operaciones/entradaalmacen.html", {
            'formulario': formulario
        })


# Funcion para acceder a la pagina de ingreso de materias primas al sistema
# gerente
@login_required(login_url="/inventarios/ingresar")
def nuevomaterial(request):
    if request.method == "POST":
        # Crea el formulario y obtiene la informacion introducida para guardar
        # en base de datos
        formulario = forms.NuevoProducto(request.POST)
        # Si el formulario es valido, guarda el nuevo producto
        if formulario.is_valid():
            formulario.save()
            return render(request, "inventarios/gerente.html", {
                "mensaje": "Producto Nuevo Ingresado en la Base de Datos"
            })
        else:
            formulario = forms.NuevoProducto()
            return render(request, "operaciones/nuevomaterial.html", {
                'formulario': formulario,
                "mensaje": "Verifique los datos ingresados"
            })
    else:
        formulario = forms.NuevoProducto()
        return render(request, "operaciones/nuevomaterial.html", {
            'formulario': formulario
        })
        

# Funcion para editar un determinado producto
@login_required(login_url="/inventarios/ingresar")
# Recibe codigo_producto como argumento para redireccionar a la pagina de un
# determinado producto
def editarproducto(request, codigo_producto):
    # Variable para obtener los datos de un proyecto especifico
    producto = Materia_prima.objects.get(
        codigo_producto=codigo_producto)
    # Si el metodo es post
    if request.method == "POST":
        # Pasa los datos de proyecto al modelo y si hay cambios actualiza
        # datos
        formulario = forms.EditarProducto(
            request.POST or None, instance=producto)
        # Validacion
        if formulario.is_valid():
            formulario.save()
            return render(request, "inventarios/gerente.html", {
                'mensaje': "Se han actualizado los datos del material!"
            })
        else:
            return render(request, "operaciones/editarproducto.html", {
                'producto': producto,
                'mensaje': "Ups. Algo Salió Mal!"
            })
    # Si el metodo es GET, envia el parametro formulario y los datos del
    # producto al modelo EditarProducto para mostrar en la pagina
    # editarproducto.html
    else:
        formulario = forms.EditarProducto(instance=producto)
        return render(request, "operaciones/editarproducto.html", {
            'producto': producto,
            'formulario': formulario
        })


# Funcion para ingresar nuevos contratistas gerente
@login_required(login_url="/inventarios/ingresar")
def nuevocontratista(request):
    if request.method == "POST":
        # Crea el formulario y obtiene la informacion introducida para guardar
        # en base de datos
        formulario = forms.NuevoContratista(request.POST)
        # Si el formulario es correcto, guarda el nuevo proveedor
        if formulario.is_valid():
            formulario.save()
            return render(request, "inventarios/gerente.html", {
                "mensaje": "Contratista Guardado Exitosamente!"
            })
        else:
            formulario = forms.NuevoContratista()
            return render(request, "operaciones/nuevocontratista.html", {
                "formulario": formulario,
                'mensaje': "El contratista ya existe. Cambie los datos."
            })
    else:
        formulario = forms.NuevoContratista()
        return render(request, "operaciones/nuevocontratista.html", {
            "formulario": formulario
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
            formulario = forms.NuevoProveedor()
            return render(request, "operaciones/nuevoproveedor.html", {
                "formulario": formulario,
                'mensaje': "El proveedor ya existe. Cambie los datos."
            })
    else:
        formulario = forms.NuevoProveedor()
        return render(request, "operaciones/nuevoproveedor.html", {
            "formulario": formulario
        })


# Funcion para editar un determinado proveedor
@login_required(login_url="/inventarios/ingresar")
# Recibe codigo_proveedor como argumento para redireccionar a la pagina de un
# determinado proveedor
def editarproveedor(request, codigo_proveedor):
    # Variable para obtener los datos de un proyecto especifico
    proveedor = Proveedores.objects.get(
        codigo_proveedor=codigo_proveedor)
    # Si el metodo es post
    if request.method == "POST":
        # Pasa los datos del proveedor al modelo y si hay cambios actualiza
        # datos
        formulario = forms.EditarProveedor(
            request.POST or None, instance=proveedor)
        # Validacion
        if formulario.is_valid():
            formulario.save()
            return render(request, "inventarios/gerente.html", {
                'mensaje': "Datos del Proyecto Actualizados Exitosamente!"
            })
        else:
            return render(request, "operaciones/editarproveedor.html", {
                'proyecto': proveedor,
                'mensaje': "Ups. Algo Salió Mal!"
            })
    # Si el metodo es GET, envia el parametro formulario y los datos del
    # proveedor al modelo EditarProveedor para mostrar en la pagina
    # editarproveedor.html
    else:
        formulario = forms.EditarProveedor(instance=proveedor)
        return render(request, "operaciones/editarproveedor.html", {
            'proveedor': proveedor,
            'formulario': formulario
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
            formulario = forms.NuevoProyecto()
            return render(request, "operaciones/nuevoproyecto.html", {
                "formulario": formulario,
                'mensaje': "Este Proyecto ya Existe. Verifique los Datos Ingresados."
            })
    else:
        formulario = forms.NuevoProyecto()
        return render(request, "operaciones/nuevoproyecto.html", {
            'formulario': formulario
        })


# Funcion para editar un determinado proyecto
@login_required(login_url="/inventarios/ingresar")
# Recibe codigo_proyecto como argumento para redireccionar a la pagina de un
# determinado proyecto
def editarproyecto(request, codigo_proyecto):
    # Variable para obtener los datos de un proyecto especifico
    proyecto = Proyectos.objects.get(
        codigo_proyecto=codigo_proyecto)
    # Si el metodo es post
    if request.method == "POST":
        # Pasa los datos de proyecto al modelo y si hay cambios actualiza
        # datos
        formulario = forms.EditarProyecto(request.POST or None, instance=proyecto)
        # Validacion
        if formulario.is_valid():
            formulario.save()
            return render(request, "inventarios/gerente.html", {
                'mensaje': "Datos del Proyecto Actualizados Exitosamente!"
            })
        else:
            return render(request, "operaciones/editarproyecto.html", {
                'proyecto': proyecto,
                'mensaje': "Ups. Algo Salió Mal!"
            })
    # Si el metodo es GET, envia el parametro formulario y los datos del
    # proyecto al modelo EditarProveedor para mostrar en la pagina
    # editarproyecto.html
    else:
        formulario = forms.EditarProyecto(instance=proyecto)
        return render(request, "operaciones/editarproyecto.html", {
            'proyecto': proyecto,
            'formulario': formulario
        })


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
            'mensaje': "El Contratista se ha Eliminado de Base de Datos!"
        })
    else:
        return render(request, "operaciones/borrarcontratista.html", {
            'contratista': contratista
        })

#################################################################33PENDIENTE POR CORREGIR TODO ESTO#############3333
#############################################################################################################################\
#############################################################################################################################\
# Funcion para editar un determinado contratista
@login_required(login_url="/inventarios/ingresar")
# Recibe codigo_contratista como argumento para redireccionar a la pagina de un
# determinado contratista
def editarcontratista(request, codigo_contratista):
    contratista = Contratistas.objects.get(
        codigo_contratista=codigo_contratista)
    if request.method == "POST":
        # Pasa los datos de contratista al modelo y si hay cambios actualiza
        # datos
        formulario = Contratistas(request.POST, contratista=contratista)
        # Validacion de datos
        if formulario.is_valid:
            # Guarda los cambios
            formulario.save()
            return render(request, "inventarios/gerente.html", {
                'mensaje': "Datos del contratista actualizados con éxito!"
            })
    else:
        return render(request, "operaciones/editarcontratista.html", {
            'contratista': contratista
        })
#############################################################################################################################\
#############################################################################################################################\
#############################################################################################################################\


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
