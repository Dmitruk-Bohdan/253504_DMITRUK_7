# Generated by Django 5.0.4 on 2024-09-16 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_alter_partner_image_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 16, 14, 31, 21, 244869)),
        ),
    ]
