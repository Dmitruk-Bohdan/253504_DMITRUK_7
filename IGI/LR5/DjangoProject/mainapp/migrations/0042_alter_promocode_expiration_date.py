# Generated by Django 5.1.1 on 2024-09-17 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0041_alter_product_pickup_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 17, 19, 55, 14, 636970)),
        ),
    ]
