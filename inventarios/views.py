from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "inventarios/index.html")


def mision(request):
    return render(request, "inventarios/mision.html")


def vision(request):
    return render(request, "inventarios/vision.html")


def contacto(request):
    return render(request, "inventarios/contacto.html")


def ingresar(request):
    return render(request, "inventarios/ingresar.html")
