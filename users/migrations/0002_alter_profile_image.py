# Generated by Django 4.0.1 on 2022-04-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='aerial.jpg', upload_to='profile_pics'),
        ),
    ]
