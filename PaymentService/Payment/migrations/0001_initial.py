# Generated by Django 3.1.2 on 2020-10-18 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DEBITCARD', 'Debit Card'), ('CREDITCARD', 'Credit Card'), ('NETBANKING', 'Netbanking'), ('CASHONDELIVERY', 'Cash on Delivery')], default='CASHONDELIVERY', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionid', models.CharField(max_length=300)),
                ('orderid', models.CharField(max_length=200)),
                ('userid', models.CharField(max_length=200)),
                ('transaction_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('response', models.CharField(max_length=2000)),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Payment.paymentmode')),
            ],
        ),
    ]
