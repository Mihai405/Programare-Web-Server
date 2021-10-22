from django.shortcuts import render
from rest_framework import viewsets
from .models import CartItem
from .serializer import CartItemSerializer
from rest_framework.response import Response

class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(CartItem.objects.filter(user=request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)