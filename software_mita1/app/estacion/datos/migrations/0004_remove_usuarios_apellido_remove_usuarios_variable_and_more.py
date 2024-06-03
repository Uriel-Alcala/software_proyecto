# Generated by Django 5.0.6 on 2024-05-30 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0003_alter_usuarios_variable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='variable',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='estacion',
            field=models.CharField(choices=[('1', 'Estacion meteorologica 1 Ojocaliente ')], default='1', max_length=1, verbose_name='Estacion'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='procedencia',
            field=models.CharField(choices=[('1', 'Universidad Autonoma de Zacatecas'), ('2', 'Sector privado'), ('3', 'Sector publico')], default='1', max_length=1, verbose_name='Procedencia'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='clave',
            field=models.CharField(max_length=100),
        ),
    ]