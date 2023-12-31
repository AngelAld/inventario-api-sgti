from django.db import models

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=30, unique=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length=30, unique=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Marca(models.Model):
    name = models.CharField(max_length=30, unique=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Item(models.Model):
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca_id = models.ForeignKey(Marca, on_delete=models.CASCADE)
    especificaciones = models.TextField(blank=True)
    status = models.CharField(max_length=30)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.categoria_id.name} - {self.marca_id.name}'