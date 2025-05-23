# Generated by Django 5.2 on 2025-05-02 13:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('biografia', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('fecha_publicacion', models.DateField()),
                ('disponible', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='libros.autor')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='libros', to='libros.categoria')),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(auto_now_add=True)),
                ('fecha_devolucion_esperada', models.DateField()),
                ('fecha_devolucion_real', models.DateField(blank=True, null=True)),
                ('devuelto', models.BooleanField(default=False)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos', to='libros.libro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
