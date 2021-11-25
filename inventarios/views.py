from django.shortcuts import render
# Importa para crear el formulario de autenticacion de usuarios.
from django.contrib.auth.forms import AuthenticationForm, UsernameField
# Importa para usar las funciones de log in y log out.
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Importa el modelo de usuarios para despues enviarlo como argumento a las
# paginas en que se requiera
from .models import CustomUser


# Create your views here.
def index(request):
    return render(request, "inventarios/index.html")


def mision(request):
    return render(request, "inventarios/mision.html")


def vision(request):
    return render(request, "inventarios/vision.html")


def contacto(request):
    return render(request, "inventarios/contacto.html")


# Funcio para ingresar usuarios y autenticar credenciales
def ingresar(request):
    # Si el usuario accede via POST
    if request.method == "POST":
        # Crea el formulario de autenticacion. Este requiere incluir el
        # parametro (data=request.POST)
        formulario = AuthenticationForm(data=request.POST)
        # Validacion
        if formulario.is_valid():
            # Permite el ingreso al usuario
            # Obtiene los datos del usuario de las variables del formulario
            usuario = formulario.get_user()
            # Ingresa en la pagina web usando la variable usuario como
            # parametro
            if usuario.pk == 1:  # Perfil del Gerente
                login(request, usuario)
                return render(request, "inventarios/gerente.html")
            # Ingresa al perfil del almacenista
            elif usuario.pk == 2:
                login(request, usuario)
                return render(request, "inventarios/almacenista.html")
            # Ingresa al perfil del director operativo
            elif usuario.pk == 3:
                login(request, usuario)
                return render(request, "inventarios/directoroperativo.html")
                # Ingresa al perfil de cada contratista
            else:
                login(request, usuario)
                return render(request, "inventarios/contratista.html")

        # Si la validacion del formulario no es correcta, se retorna a la 
        # pagina de inicio de sesion
        else:
            return render(request, "inventarios/ingresar.html", {
                "formulario": formulario,
                "mensaje": "Upss. Algo salió mal. Su usuario o contraseña no son correctos.Vuelva a Intentar!",
            })

    # Si el usuario accede via GET
    else:
        # Crea y muestra el formulario de inicio de sesion
        formulario = AuthenticationForm()
        return render(request, "inventarios/ingresar.html", {
            "formulario": formulario,
        })


# Funcion para cerrar sesion
def salir_view(request):
    if request.method == "POST":
        logout(request)
        return render(request, "inventarios/index.html", {
            "mensaje": "Sesión cerrada con éxito!",
        })
        

@login_required(login_url=ingresar)
def gerente(request):
    usuario = CustomUser.objects.all()
    return render(request, "inventarios/gerente.html", {
        'usuario': usuario,
    })


@login_required(login_url=ingresar)
def almacenista(request):
    usuario = CustomUser.objects.all()
    return render(request, "inventarios/almacenista.html", {
        'usuario': usuario,
    })


@login_required(login_url=ingresar)
def directoroperativo(request):
    usuario = CustomUser.objects.all()
    return render(request, "inventarios/directoroperativo.html", {
        'usuario': usuario,
    })


@login_required(login_url=ingresar)
def contratista(request):
    usuario = CustomUser.objects.all()
    return render(request, "inventarios/contratista.html", {
        'usuario': usuario,
    })
