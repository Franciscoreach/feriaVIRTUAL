# Generated by Django 4.1.1 on 2022-10-26 17:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feriavirtualweb', '0011_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudproducto',
            name='cantidadKG',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(500)], verbose_name='Cantidad de Kilos'),
        ),
        migrations.AlterField(
            model_name='solicitudproducto',
            name='estadoSolicitud',
            field=models.CharField(choices=[('EN PROCESO', 'En Proceso'), ('ACEPTADA', 'Aceptada'), ('RECHAZADA', 'Rechazada')], default='EN PROCESO', max_length=15),
        ),
        migrations.AlterField(
            model_name='subastaproducto',
            name='estadoSubasta',
            field=models.CharField(choices=[('EN PROCESO', 'En Proceso'), ('ACEPTADA', 'Aceptada'), ('RECHAZADA', 'Rechazada')], default='EN PROCESO', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre de Usuario'),
        ),
    ]
