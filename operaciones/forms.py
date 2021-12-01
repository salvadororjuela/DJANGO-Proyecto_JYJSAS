from django import forms
""" Como los modelos a usar estan en la carpeta de la aplicacion inventarios se
deben importar a la carpeta de la aplicacion operaciones para poder hacer uso
de ellos en los formularios que van a ir en las diferentes paginas web de
operaciones """
from . import models


# Clase para insertar los datos en los modelos Movimientos_Almacen y
# Materia_prima al ingresar nuevos productos al almacen.
class NuevoProducto(forms.ModelForm):
    class Meta:
        # Define los campos a presetar y el modelo del que heredan.
        model = models.Materia_prima
        # Campos a mostrar
        fields = ['codigo_producto', 'nombre_producto',
                  'numero_factura_compra', 'cantidad', 'unidad_de_medida',
                  'precio', 'marca', 'Proveedores_cod_proveedor'
                  ]


# Clase para insertar datos de nuevos proveedores
class NuevoProveedor(forms.ModelForm):
    class Meta:
        # Define los campos a presentar y el modelo que heredan
        model = models.Proveedores
        # Campos del formulario
        fields = [
            'codigo_proveedor', 'nombre_proveedor', 'direccion_proveedor',
            'barrio_proveedor', 'ciudad_proveedor', 'telefono_proveedor',
            'website_proveedor', 'email', 'maneja_credito'
        ]


# Clase para editar proveedores
class EditarProveedor(forms.ModelForm):
    class Meta:
        # Modelo del que hereda
        model = models.Proveedores
        # Campos del formulario
        fields = [
            'nombre_proveedor', 'direccion_proveedor', 'barrio_proveedor',
            'ciudad_proveedor', 'telefono_proveedor', 'website_proveedor',
            'email', 'maneja_credito'
        ]


# Clase para insertar nuevos proyectos
class NuevoProyecto(forms.ModelForm):
    class Meta:
        # Define los campos a presentar y el modelo que heredan
        model = models.Proyectos
        # Campos del formulario
        fields = [
            'codigo_proyecto', 'nombre_proyecto', 'direccion_proyecto',
            'descripcion_proyecto', 'estado_proyecto', 'empleado_responsable'
        ]


# Clase para editar proyectos
class EditarProyecto(forms.ModelForm):
    class Meta:
        # Modelo del que hereda
        model = models.Proyectos
        fields = [
            'nombre_proyecto', 'direccion_proyecto', 'descripcion_proyecto',
            'estado_proyecto', 'empleado_responsable'
        ]
