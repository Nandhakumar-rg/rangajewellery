# Generated by Django 4.0.3 on 2022-07-29 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_product_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
