# Generated by Django 4.0.3 on 2022-07-29 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_itemcart_uname'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]