# Generated by Django 4.1.7 on 2023-04-25 23:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion_tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bl_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombProducto', models.CharField(default='', max_length=32)),
                ('codProducto', models.CharField(default='', max_length=32)),
                ('precioCompra', models.FloatField(default='', max_length=10)),
                ('precioVenta', models.FloatField(default='', max_length=10)),
                ('usuarioProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='bl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolUsuario', models.CharField(default='VENDEDOR', max_length=15)),
                ('nroCelular', models.CharField(default='', max_length=15)),
                ('fechaIngreso', models.DateField(default=datetime.date.today)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='datosUsuario',
        ),
    ]
