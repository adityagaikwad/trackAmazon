from django.db import models
from django.forms import ModelForm


# USE DB BROWSER for SQLite to modify tables


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):  # __unicode__ on Python 2
        return self.username


# stores all products being tracked by all users
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_url = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=100, blank=True)
    asin = models.CharField(max_length=50, blank=True)
    img_url = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    # updated_at = models.DateTimeField()
    
    def __str__(self):  # __unicode__ on Python 2
        return self.title


# Graph model stores everyday's updated price of products in Product model
class Graph(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    current_price = models.DecimalField(max_digits=20, decimal_places=2)


# has price when user started tracking
class User_products(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_when_added = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    price_drop_below = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    email_to = models.CharField(max_length=50)
