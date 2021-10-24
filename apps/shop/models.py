from django.db import models
from apps.users.models import User
from apps.products.models import Product
import datetime

class CartItem(models.Model):
    product  =  models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=1)
    placedDate = models.DateField(auto_now_add=True)
    cartItems = models.ManyToManyField(CartItem)