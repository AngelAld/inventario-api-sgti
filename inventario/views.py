from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .serializer import AreaSerializer, CategoriaSerializer, MarcaSerializer, ItemSerializer
from .models import Area, Categoria, Marca, Item

# Create your views here.


class AreaView(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    pagination_class = LimitOffsetPagination

class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    pagination_class = LimitOffsetPagination

class MarcaView(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    pagination_class = LimitOffsetPagination

class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = LimitOffsetPagination
