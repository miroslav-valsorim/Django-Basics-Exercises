# Generated by Django 5.0.2 on 2024-03-03 15:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch_clothes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderclothes',
            name='category',
            field=models.CharField(choices=[('Shirt', 'Shirt'), ('Jacket', 'Jacket'), ('Shorts', 'Shorts')], default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderclothes',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
