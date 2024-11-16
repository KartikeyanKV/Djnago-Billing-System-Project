# Generated by Django 5.1.3 on 2024-11-12 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
        ('Ordermanagement', '0002_customer_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=200, null=True)),
                ('order_date', models.DateField(null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('amount', models.FloatField(default=0)),
                ('gst', models.FloatField(default=0)),
                ('bill_amount', models.FloatField(default=0)),
                ('Product_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventory.products')),
                ('customer_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ordermanagement.customer')),
            ],
        ),
    ]