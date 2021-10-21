from django.db import models

def nameFile(instance, filename):
    return f'products/{instance.id}/{filename}'

class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=255,default='')
    productImage = models.ImageField(upload_to=nameFile)

    def __str__(self):
        return self.name
