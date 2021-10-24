from django.shortcuts import render
from rest_framework import viewsets
from .models import CartItem,Order
from .serializer import ListCartItemSerializer,CreateCartItemSerializer,CreateOrderSerializer,ListOrderSerializer
from rest_framework.response import Response

class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = ListCartItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(CartItem.objects.filter())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        write_serializer = CreateCartItemSerializer(data=request.data , context={'request': request})
        write_serializer.is_valid(raise_exception=True)
        instance = write_serializer.save()
        read_serializer=ListCartItemSerializer(instance)
        return Response(read_serializer.data)

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = ListOrderSerializer

    def create(self, request, *args, **kwargs):
        write_serializer = CreateOrderSerializer(data=request.data, context={'request': request})
        write_serializer.is_valid(raise_exception=True)
        instance = write_serializer.save()
        read_serializer = ListOrderSerializer(instance)
        return Response(read_serializer.data)

