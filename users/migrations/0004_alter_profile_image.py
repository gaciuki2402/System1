# Generated by Django 4.0.1 on 2022-04-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/media/profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
