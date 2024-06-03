# Generated by Django 5.0.6 on 2024-05-30 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0004_remove_usuarios_apellido_remove_usuarios_variable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='estacion',
            field=models.CharField(choices=[('1', 'Estacion meteorologica 1 Ojocaliente ')], default='0', max_length=1, verbose_name='Estacion'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='procedencia',
            field=models.CharField(choices=[('1', 'Universidad Autonoma de Zacatecas'), ('2', 'Sector privado'), ('3', 'Sector publico')], default='0', max_length=1, verbose_name='Procedencia'),
        ),
    ]
