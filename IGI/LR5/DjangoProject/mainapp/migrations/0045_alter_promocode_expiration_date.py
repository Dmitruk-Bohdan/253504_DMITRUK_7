# Generated by Django 5.0.4 on 2024-09-18 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0044_remove_promocode_image_remove_promocode_max_usage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 18, 14, 26, 35, 614348)),
        ),
    ]
