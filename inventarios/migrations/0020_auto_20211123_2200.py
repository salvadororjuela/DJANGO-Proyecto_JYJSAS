# Generated by Django 3.2.7 on 2021-11-24 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0019_alter_proyectos_contratista_asignado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectos',
            name='contratista_asignado',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='nombre_proyecto',
        ),
        migrations.AddField(
            model_name='proyectos',
            name='contratistas',
            field=models.ManyToManyField(to='inventarios.Contratistas'),
        ),
        migrations.AlterField(
            model_name='ordenes_salida_materiaprima',
            name='codigo_producto',
            field=models.IntegerField(),
        ),
    ]