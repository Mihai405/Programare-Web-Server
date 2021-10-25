from rest_framework import serializers
from apps.users.serializer import UserSerializer
from apps.users.models import User
from apps.products.serializer import ProductSerializer
from apps.products.serializer import Product
from .models import CartItem , Order
from django.db import transaction

class CreateCartItemSerializer(serializers.ModelSerializer):
    product  =  serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(many=False , read_only=True)
    class Meta:
        model = CartItem
        fields = ['id','product','quantity','user']
    def create(self,validated_data):
        request = self.context.get('request', None)
        user = request.user
        with transaction.atomic():
            cartItem = CartItem.objects.create(user=user, **validated_data)
        return cartItem



class ListCartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model=CartItem
        fields=['id','product','quantity','ordered']

class CreateOrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    cartItems=serializers.PrimaryKeyRelatedField(queryset=CartItem.objects.all(), many=True)
    class Meta:
        model = Order
        fields='__all__'

    def create(self,validated_data):
        request = self.context.get('request', None)
        user = request.user
        with transaction.atomic():
            cartItems_data = validated_data.pop('cartItems')
            order = Order.objects.create(user=user, **validated_data)
            for cartItem in cartItems_data:
                order.cartItems.add(cartItem)
        return order

class ListOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cartItems = ListCartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
