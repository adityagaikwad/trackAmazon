from django.db import models

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
class Product(models.Model):
    user_id = models.ForeignKey(Login, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    asin = models.CharField(max_length=50)
    current_price = models.PositiveIntegerField()
    increase = models.PositiveIntegerField()
    decrease = models.PositiveIntegerField()
    img_url = models.CharField(max_length=500)