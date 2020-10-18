from django.db import models
import jsonfield

# Create your models here.


class Order(models.Model):
    order_date = models.DateField(null=False)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    userid = models.CharField(max_length=20, null=False)
    product_details = jsonfield.JSONField()
    payment_details = jsonfield.JSONField()


