from django.contrib import admin

# Register your models here.
from .models import Transaction, PaymentMode

admin.site.register(Transaction)
admin.site.register(PaymentMode)