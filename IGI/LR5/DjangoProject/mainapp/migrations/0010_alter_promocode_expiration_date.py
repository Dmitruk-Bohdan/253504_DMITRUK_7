# Generated by Django 5.0.4 on 2024-05-10 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_profile_birth_date_alter_promocode_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 9, 17, 45, 37, 179095)),
        ),
    ]
