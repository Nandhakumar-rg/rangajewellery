# Generated by Django 4.0.3 on 2022-07-29 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_sign_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='profile_pic',
            field=models.ImageField(default='https://i.pinimg.com/originals/51/f6/fb/51f6fb256629fc755b8870c801092942.png', upload_to='images/profiles'),
        ),
    ]