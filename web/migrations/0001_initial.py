# Generated by Django 5.0.3 on 2024-03-26 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tbl_area',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tbl_categoria',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField(null=True)),
                ('detalle', models.TextField(null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('size_disponible', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=150)),
                ('tecnologia_fabricada', models.CharField(max_length=255)),
                ('color_disponible', models.CharField(max_length=255)),
                ('musical', models.CharField(max_length=200)),
                ('luces_interno', models.CharField(max_length=200)),
                ('personalizable', models.CharField(max_length=255)),
                ('popularidad', models.DecimalField(decimal_places=1, max_digits=4)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.area')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.categoria')),
            ],
            options={
                'db_table': 'tbl_producto',
            },
        ),
    ]
