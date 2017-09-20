from django.db import models
from django.forms import ModelForm

# USE DB BROWSER for SQLite to modify tables

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    
class Product(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_url = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=100, blank=True)
    asin = models.CharField(max_length=50, blank=True)
    current_price = models.PositiveIntegerField()
    increase = models.PositiveIntegerField()
    decrease = models.PositiveIntegerField()
    img_url = models.CharField(max_length=500, blank=True)
    
# class RegisterForm(ModelForm):
#     class Meta:
#         model = Users
#         fields = ['username', 'email', 'password']