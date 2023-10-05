from django.shortcuts import render
from rest_framework import viewsets
from .serializer import AreaSerializer, CategoriaSerializer, MarcaSerializer, ItemSerializer
from .models import Area, Categoria, Marca, Item
# Create your views here.


class AreaView(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaView(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
