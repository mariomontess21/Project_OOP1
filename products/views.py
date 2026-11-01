from django.shortcuts import render
from rest_framework import viewsets
from .models import Products
from .serializer import ProductsSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    model = Products
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return Products.objects.all()

