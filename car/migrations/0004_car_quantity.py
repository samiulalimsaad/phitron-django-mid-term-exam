# Generated by Django 5.0 on 2023-12-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
