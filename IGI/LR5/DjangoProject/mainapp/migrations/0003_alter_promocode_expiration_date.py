# Generated by Django 5.0.4 on 2024-05-09 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_pickuppoint_promocode_vacancy_remove_sale_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 8, 18, 17, 33, 648209)),
        ),
    ]
