# Generated by Django 5.0.3 on 2024-03-13 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_order', '0005_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='items',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, to='cart_order.shoppingcart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart_order.customer'),
        ),
    ]
