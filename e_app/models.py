from django.contrib.auth.models import AbstractUser
from django.db import models
class Login_view(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
class Customer(models.Model):
    user=models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name='customer')
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()
    status1=models.BooleanField(default=0)
    document = models.FileField(upload_to='documents/')
class Seller(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='seller')
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
    document = models.FileField(upload_to='documents/')

class Product(models.Model):
    user = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='product')
    product_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.FileField(upload_to='documents/')
    description = models.TextField()













