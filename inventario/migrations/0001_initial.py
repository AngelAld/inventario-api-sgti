# Generated by Django 4.2.6 on 2023-10-04 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('especificaciones', models.TextField(blank=True)),
                ('status', models.CharField(max_length=30)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.area')),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.categoria')),
                ('marca_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.marca')),
            ],
        ),
    ]
