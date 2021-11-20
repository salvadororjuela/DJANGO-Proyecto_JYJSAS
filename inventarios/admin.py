from django.contrib import admin
from .models import Materia_prima, Movimientos_Almacen, Proveedores
from .models import Ordenes_pedido_materiaprima, Facturas
from .models import Ordenes_salida_materiaprima
from .models import Proyectos, Contratistas
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Modificar la vista por defecto de usuarios en admin
class CustomUserAdmin(UserAdmin):
    pass
    list_display = (
        'username', 'codigo_empleado', 'first_name', 'last_name', 'is_staff',
        'cargo_empleado', 'telefono_empleado', 'correo_empleado'
    )

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
            'fields': ('codigo_empleado', 'cargo_empleado', 'telefono_empleado')
        })
    )

    # add_fieldsets = (
    #     (None, {
    #         'fields': ('Usuario', 'Contraseña1', 'Contraseña2')
    #     }),
    #     ('Informacion Personal', {
    #         'fields': ('Nombres', 'Apellidos', 'correo_empleado')
    #     }),
    #     ('Permisos', {
    #         'fields': (
    #             'is_active', 'is_staff', 'is_superuser',
    #             'groups', 'user_permissions'
    #         )
    #     }),
    #     ('Fechas Importantes', {
    #         'fields': ('Ultimo_login', 'Fecha_login')
    #     }),
    #     ('Informacion adicional', {
    #         'fields': ('codigo_empleado', 'cargo_empleado', 'telefono_empleado')
    #     })
    # )


admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
admin.site.register(Materia_prima)
admin.site.register(Movimientos_Almacen)
admin.site.register(Proveedores)
admin.site.register(Ordenes_pedido_materiaprima)
admin.site.register(Facturas)
admin.site.register(Ordenes_salida_materiaprima)
admin.site.register(Proyectos)
admin.site.register(Contratistas)
