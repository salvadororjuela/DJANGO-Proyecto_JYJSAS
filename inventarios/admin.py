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
        'username', 'codigo_empleado', 'first_name', 'last_name', 'is_staff',
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
            'fields': ('codigo_empleado', 'cargo_empleado',
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
            'fields': ('codigo_empleado', 'cargo_empleado',
                       'telefono_empleado')
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
admin.site.register(Materia_prima)
admin.site.register(Movimientos_Almacen)
admin.site.register(Proveedores)
admin.site.register(ordenes_pedido_materiaprima)
admin.site.register(ordenes_salida_materiaprima)
admin.site.register(Proyectos)
admin.site.register(Contratistas)
