# Generated by Django 3.2.7 on 2021-11-24 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0004_rename_codigo_empleado_customuser_identificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenes_salida_materiaprima',
            name='cod_movimiento_salida',
        ),
        migrations.AddField(
            model_name='ordenes_salida_materiaprima',
            name='cod_movimiento_salida',
            field=models.ForeignKey(default='00000000', on_delete=django.db.models.deletion.CASCADE, to='inventarios.movimientos_almacen'),
        ),
    ]