# Generated by Django 3.2.7 on 2021-11-25 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratistas',
            name='apellido_contratista',
            field=models.CharField(default='', max_length=50),
        ),
    ]