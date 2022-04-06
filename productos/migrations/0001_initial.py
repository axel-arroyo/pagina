# Generated by Django 3.2.7 on 2021-11-30 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('slug', models.SlugField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('slug', models.SlugField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=128)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('slug', models.SlugField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('stock', models.IntegerField(default=1, verbose_name='Stock')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('descripcion', models.CharField(default='', max_length=512, verbose_name='Descripcion')),
                ('vendidos', models.IntegerField(default=0, verbose_name='Vendidos')),
                ('creado_el', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('actualizado_el', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria', verbose_name='Categoría')),
                ('subcategoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.subcategoria', verbose_name='Subcategoría')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='productos', verbose_name='Imagen')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='productos.item', verbose_name='Item')),
            ],
        ),
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracterisica', models.CharField(max_length=128, verbose_name='Caracteristica')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.item', verbose_name='Item')),
            ],
        ),
    ]