# Generated by Django 3.2.7 on 2021-11-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0002_contratistas_apellido_contratista'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratistas',
            name='identificacion',
            field=models.IntegerField(default='000000000'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cargo_empleado',
            field=models.CharField(choices=[('DG', 'Director General'), ('DO', 'Director Operacional'), ('AL', 'Almacenista'), ('CO', 'Contratista'), ('NA', 'No Asignado')], default='NA', max_length=50),
        ),
    ]