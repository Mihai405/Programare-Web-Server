from rest_framework import serializers
from apps.users.serializer import UserSerializer
from apps.users.models import User
from apps.products.serializer import ProductSerializer
from apps.products.serializer import Product
from .models import CartItem
from django.db import transaction

class CartItemSerializer(serializers.ModelSerializer):
    product  =  serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(many=False , read_only=True)
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields=['placedDate']
    def create(self,validated_data):
        request = self.context.get('request', None)
        user = request.user
        with transaction.atomic():
            cartItem = CartItem.objects.create(user=user, **validated_data)
        return cartItem