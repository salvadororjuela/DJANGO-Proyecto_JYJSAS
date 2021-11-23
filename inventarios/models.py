from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ManyToManyField


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
    cargo_empleado = models.CharField(
        max_length=50, choices=cargos, default="NA")
    telefono_empleado = models.BigIntegerField(default="0000000000")
    correo_empleado = models.CharField(
        max_length=50, default="empleado@ejemplo.com")


# Usada para guardar registro de los movimientos de entrada o salida de materia
# prima del almacén
class Movimientos_Almacen (models.Model):
    cod_movimiento = models.IntegerField(primary_key=True)  # llave primaria
    # Diccionario de las opciones de cargos para mostrar en admin
    movimientos = [
        ("En", "Entrada"),
        ("Sa", "Salida"),
        ("Na", "Sin Asignar Aún")
    ]
    tipo_movimiento = models.CharField(
        max_length=8, choices=movimientos, default="Na")


# Registro de proveedores
class Proveedores (models.Model):
    codigo_proveedor = models.IntegerField(primary_key=True)  # llave primaria
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
    maneja_credito = models.CharField(
        max_length=20, choices=credito, default="No")


# Usada para registrar los ingresos de materias primas al almacén
class Materia_prima (models.Model):
    codigo_producto = models.IntegerField(primary_key=True)  # llave primaria
    nombre_producto = models.CharField(max_length=100)
    numero_factura_compra = models.CharField(
        max_length=100, default="0000000000")
    cantidad = models.IntegerField(default="1")
    unidades = [
        ("Un", "Unidad"), ("Lb", "Libras"), ("Kg", "Kilogrmos"),
        ("In", "Pulgadas"), ("Cm", "Centimetros"), ("Mt", "Metros"),
        ("Pi", "Pies"), ("M2", "Metros Cuadrados"), ("M3", "Metros Cúbicos"),
        ("Lt", "Litros"), ("Ml", "Mililitros"), ("Gl", "Galones"),
        ("1/16", "1/16 de Galón"), ("1/8", "1/8 de Galón"),
        ("1/4", "1/4 de Galón"), ("1/2", "1/2 Galón"),
    ]
    unidad_de_medida = models.CharField(
        max_length=15, choices=unidades, default="Un")
    precio = models.IntegerField()
    marca = models.CharField(max_length=100, null=True)
    Proveedores_cod_proveedor = models.ForeignKey(
        Proveedores, null=False, on_delete=models.CASCADE)
    # Muchos productos pueden tener muchos movimientos de almacén y viceversa
    cod_movimiento_ingreso = ManyToManyField(Movimientos_Almacen)


# Usada cuando el empleado encargado de un proyecto solicita materia prima al
# alamacén
class Ordenes_pedido_materiaprima (models.Model):
    codigo_orden_pedido = models.IntegerField(
        primary_key=True)  # llave primaria
    codigo_producto = models.ForeignKey(
        Materia_prima, null=False, on_delete=models.CASCADE)  # llave foranea
    cantidad_pedida = models.IntegerField()
    fecha_orden_pedido = models.DateTimeField(auto_now_add=True)
    empleado_solicitante = models.ForeignKey(
        CustomUser, null=False, on_delete=models.CASCADE, default="-------")  # llave foranea


# Registro de los proyectos que tiene la compañía
class Proyectos (models.Model):
    codigo_proyecto = models.IntegerField(primary_key=True)  # llave primaria
    direccion_proyecto = models.CharField(max_length=100)
    descripcion_proyecto = models.CharField(max_length=200)
    estado = [
        ("Act", "Activo"),
        ("Ter", "Terminado"),
        ("Na", "No Asignado"),
    ]
    estado_proyecto = models.CharField(
        max_length=12, choices=estado, default="Na")
    empleado_responsable = models.ForeignKey(
        CustomUser, null=False, on_delete=models.CASCADE)  # llave foranea


# Usada para registrar las salidas de material del almacén
class Ordenes_salida_materiaprima (models.Model):
    codigo_orden_salida = models.IntegerField(
        primary_key=True)  # llave primaria
    codigo_producto = models.IntegerField()  # llave foranea
    cantidad_entregada = models.IntegerField()
    fecha_entrega_materiaprima = models.DateTimeField(auto_now_add=True)
    proyecto_destino = models.ForeignKey(
        Proyectos, null=False, on_delete=models.CASCADE)  # llave foranea
    empleado_responsable = models.ForeignKey(
        CustomUser, null=False, on_delete=models.CASCADE)  # llave foranea
    # Muchos productos pueden tener muchos movimientos de almacén y viceversa
    cod_movimiento_salida = ManyToManyField(Movimientos_Almacen)


# Registro de contratistas
class Contratistas (models.Model):
    codigo_contratista = models.IntegerField(
        primary_key=True)  # llave primaria
    nombre_contratista = models.CharField(max_length=50)
    direccion_contratista = models.CharField(max_length=100)
    correo_contratista = models.CharField(max_length=50)
    telefono_contratista = models.IntegerField()
    especialidad_contratista = models.CharField(max_length=50)
    proyecto_asignacion = models.ForeignKey(
        Proyectos, null=False, on_delete=models.CASCADE)  # Llave foranea
