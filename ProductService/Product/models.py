from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Category(models.Model):
    categoryid = models.CharField(max_length=200, unique=True, null=False)
    category_name = models.CharField(max_length=50, unique=True, null=False)
    date_posted = models.DateField(null=False)

class Product(models.Model):
    productid = models.CharField(max_length=200, unique=True, null=False)
    product_name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200)
    #image = models.ImageField(upload_to='Products')
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0, null=False)
    regular_price = models.DecimalField(default=0, decimal_places=2, max_digits=10, null=False)
    discounted_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    product_rating = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    product_review = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ManyToManyField(Category)
    vendor = models.CharField(max_length=200, null=False)
