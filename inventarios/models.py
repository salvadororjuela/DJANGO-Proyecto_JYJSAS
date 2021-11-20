from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Modelo modificado para usuarios en admin
class CustomUser(AbstractUser):
    codigo_empleado = models.BigIntegerField(
        default="0000000000")  # llave primaria
    # Diccionario de las opciones de cargos para mostrar en admin
    cargos = [
        ("DG", "Director General"),
        ("DO", "Director Operacional"),
        ("AL", "Almacenista"),
        ("PR", "Proveedor"),
        ("CO", "Contratista"),
        ("NA", "No Asignado")
    ]
    # choices toma los valores de la lista cargos (arriba declarada) y crea una
    # lista desplegable de los cargos en admin
    cargo_empleado = models.CharField(max_length=50, choices=cargos, default="NA")
    telefono_empleado = models.BigIntegerField(default="0000000000")
    correo_empleado = models.CharField(
        max_length=50, default="empleado@ejemplo.com")


class Materia_prima (models.Model):
    codigo_producto = models.IntegerField()  # llave primaria
    nombre_producto = models.CharField(max_length=100)
    cantidad_almacen = models.IntegerField()
    cantidad_minima = models.IntegerField()
    unidad_de_medida = models.CharField(max_length=15)
    seccion_ubicacion_material = models.CharField(max_length=50)
    precio = models.IntegerField()
    orden_pedido = models.IntegerField()
    Almacen_cod_movimiento = models.IntegerField()
    Proveedores_cod_proveedor = models.IntegerField()


class Movimientos_Almacen (models.Model):
    cod_movimiento = models.IntegerField()  # llave primaria
    tipo_movimiento = models.CharField(max_length=50)


class Proveedores (models.Model):
    codigo_proveedor = models.IntegerField()  # llave primaria
    nombre_proveedor = models.CharField(max_length=50)
    direccion_proveedor = models.CharField(max_length=100)
    barrio_proveedor = models.CharField(max_length=50)
    ciudad_proveedor = models.CharField(max_length=50)
    telefono_proveedor = models.IntegerField()
    website_proveedor = models.CharField(max_length=50)
    # Diccionario de las opciones disponibles de crédito para mostrar en admin
    credito = [
        ("Si", "Si Maneja Crédito"),
        ("No", "No Ofrece Crédito"),
    ]
    # choices toma los valores de la lista cargos (arriba declarada) y crea una
    # lista desplegable de las opciones de crédito
    maneja_credito = models.CharField(max_length=20, choices=credito, default="No")


class Ordenes_pedido_materiaprima (models.Model):
    codigo_orden_pedido = models.IntegerField()  # llave primaria
    codigo_producto = models.IntegerField()  # llave foranea
    cantidad_pedida = models.IntegerField()
    fecha_orden_pedido = models.DateTimeField(auto_now_add=True)
    proveedores_codigo = models.IntegerField()  # llave foranea


class Facturas (models.Model):
    codigo_factura = models.IntegerField()  # llave primaria
    fecha_factura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Código Factura: {self.codigo_factura} - Fecha: {self.fecha_factura}"


class Ordenes_salida_materiaprima (models.Model):
    codigo_orden_salida = models.IntegerField()  # llave primaria
    codigo_producto = models.IntegerField()  # llave foranea
    cantidad_entregada = models.IntegerField()
    fecha_entrega_materiaprima = models.DateTimeField(auto_now_add=True)
    proyecto_destino = models.IntegerField()  # llave foranea
    codigo_movimiento = models.IntegerField()  # llave foranea
    empleado_responsable = models.IntegerField()  # llave foranea


class Proyectos (models.Model):
    codigo_proyecto = models.IntegerField()  # llave primaria
    direccion_proyecto = models.CharField(max_length=100)
    descripcion_proyecto = models.CharField(max_length=200)
    empleado_responsable = models.IntegerField()  # llave foranea


class Contratistas (models.Model):
    codigo_contratista = models.IntegerField()  # llave foranea
    nombre_contratista = models.CharField(max_length=50)
    direccion_contratista = models.CharField(max_length=100)
    correo_contratista = models.CharField(max_length=50)
    telefono_contratista = models.IntegerField()
    especialidad_contratista = models.CharField(max_length=50)
