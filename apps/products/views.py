from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from rest_framework.parsers import MultiPartParser
class ProductView(viewsets.ModelViewSet):
    queryset            =   Product.objects.all()
    serializer_class    =   ProductSerializer
    parser_classes      =   [MultiPartParser]