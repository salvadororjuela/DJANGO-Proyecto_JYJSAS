# Generated by Django 3.2.7 on 2021-12-01 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materia_prima',
            old_name='precio',
            new_name='precio_unitario',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cargo_empleado',
            field=models.CharField(choices=[('Gerente General', 'Director General'), ('Director Operacional', 'Director Operacional'), ('Almacenista', 'Almacenista'), ('Contratista', 'Contratista')], default='Contratista', max_length=50),
        ),
    ]
