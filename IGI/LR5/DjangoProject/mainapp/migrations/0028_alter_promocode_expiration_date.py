# Generated by Django 5.0.4 on 2024-09-16 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_remove_partner_image_alter_promocode_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 16, 14, 46, 6, 37670)),
        ),
    ]
