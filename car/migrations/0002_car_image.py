# Generated by Django 5.0 on 2023-12-16 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car/car_images/'),
        ),
    ]
