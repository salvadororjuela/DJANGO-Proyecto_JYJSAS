from django.contrib import admin
from .models import Materia_prima, Movimientos_Almacen, Proveedores
from .models import ordenes_pedido_materiaprima
from .models import ordenes_salida_materiaprima
from .models import Proyectos, Contratistas
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Modificar la vista por defecto de usuarios en admin
class CustomUserAdmin(UserAdmin):

    # Listado de los campos a mostrar en admin.
    list_display = (
        'pk', 'username', 'identificacion', 'first_name', 'last_name', 'is_staff',
        'cargo_empleado', 'telefono_empleado', 'correo_empleado'
    )

    # campos para mostrar datos de los usuarios registrados
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Informacion Personal', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permisos', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Fechas Importantes', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Informacion adicional', {
            'fields': ('identificacion', 'cargo_empleado',
                       'telefono_empleado')
        })
    )

    # Campos para agregar datos de nuevos usuarios
    add_fieldsets = (
        (None, {
            # Password1 y password2 requeridas para confirmacion de contrasena
            'fields': ('username', 'password1', 'password2')
        }),
        ('Informacion Personal', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permisos', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Fechas Importantes', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Informacion adicional', {
            'fields': ('identificacion', 'cargo_empleado',
                       'telefono_empleado')
        })
    )


class MovimientosAlmacenAdmin(admin.ModelAdmin):
    list_display = (
        'cod_movimiento', 'tipo_movimiento'
    )


class ProveedoresAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_proveedor', 'nombre_proveedor', 'direccion_proveedor',
        'telefono_proveedor', 'website_proveedor', 'maneja_credito'
    )


class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_producto', 'nombre_producto', 'numero_factura_compra',
        'cantidad', 'unidad_de_medida', 'precio', 'marca'
    )


class OrdenesPedidoMateriaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_orden_pedido', 'codigo_producto', 'cantidad_pedida',
        'fecha_orden_pedido', 'empleado_solicitante'
    )


# Vista modificada del modelo proyectos en el admin
class ProyectosAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_proyecto', 'nombre_proyecto', 'direccion_proyecto',
        'descripcion_proyecto', 'estado_proyecto', 'empleado_responsable',
    )


class OrdenesSalidaMateriaPrimaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_orden_salida', 'codigo_producto', 'cantidad_entregada',
        'fecha_entrega_materiaprima', 'proyecto_destino',
        'empleado_responsable'
    )


# Vista modificada del modelo proyectos en el admin
class ContratistasAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_contratista', 'nombre_contratista', 'direccion_contratista',
        'correo_contratista', 'telefono_contratista',
        'especialidad_contratista', 'proyecto_asignacion'
    )



# Registros Modificados
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Movimientos_Almacen, MovimientosAlmacenAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Materia_prima, MateriaPrimaAdmin)
admin.site.register(ordenes_pedido_materiaprima, OrdenesPedidoMateriaAdmin)
admin.site.register(Proyectos, ProyectosAdmin)
admin.site.register(ordenes_salida_materiaprima,
                    OrdenesSalidaMateriaPrimaAdmin)
admin.site.register(Contratistas, ContratistasAdmin)

# Register your models here.
# Registros Originales
# admin.site.register(Materia_prima)
# admin.site.register(Movimientos_Almacen)
#admin.site.register(Proveedores)
#admin.site.register(ordenes_pedido_materiaprima)
#admin.site.register(ordenes_salida_materiaprima)
#admin.site.register(Proyectos)
#admin.site.register(Contratistas)
