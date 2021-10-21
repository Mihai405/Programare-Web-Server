from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer

class ProductView(viewsets.ModelViewSet):
    queryset            =   Product.objects.all()
    serializer_class    =   ProductSerializer