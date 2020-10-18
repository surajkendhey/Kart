from django.db import models
import jsonfield

# Create your models here.

class Cart(models.Model):
    userid = models.CharField(max_length=200, null=False)
    product_details = jsonfield.JSONField()
