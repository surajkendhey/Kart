from django.db import models
import jsonfield

# Create your models here.


class PaymentMode(models.Model):
    payment_choices = [
        ('DEBITCARD', 'Debit Card'),
        ('CREDITCARD', 'Credit Card'),
        ('NETBANKING', 'Netbanking'),
        ('CASHONDELIVERY', 'Cash on Delivery'),
        ]
    type = models.CharField(max_length=20,
                            choices=payment_choices,
                            default='CASHONDELIVERY',
                            )
    details = jsonfield.JSONField()


class Transaction(models.Model):
    orderid = models.CharField(max_length=200, null=False)
    userid = models.CharField(max_length=200, null=False)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    payment_type = models.ForeignKey(PaymentMode, on_delete=models.DO_NOTHING)
    response = models.CharField(max_length=2000, null=False)

