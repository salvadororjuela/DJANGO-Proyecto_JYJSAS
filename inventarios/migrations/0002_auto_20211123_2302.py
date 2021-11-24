# Generated by Django 3.2.7 on 2021-11-24 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenes_pedido_materiaprima',
            name='codigo_producto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ordenes_salida_materiaprima',
            name='codigo_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarios.materia_prima'),
        ),
    ]