# Generated by Django 3.2.7 on 2021-12-01 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0003_auto_20211130_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradasalmacen',
            name='id',
        ),
        migrations.RemoveField(
            model_name='entradasalmacen',
            name='codigo_material',
        ),
        migrations.AddField(
            model_name='entradasalmacen',
            name='codigo_material',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='operaciones.materia_prima'),
        ),
        migrations.AlterField(
            model_name='entradasalmacen',
            name='numero_factura_compra',
            field=models.CharField(default='0000000000', max_length=100, primary_key=True, serialize=False),
        ),
    ]