# Generated by Django 4.0.3 on 2022-04-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_signup_sign'),
    ]

    operations = [
        migrations.CreateModel(
            name='move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
            ],
        ),
    ]
