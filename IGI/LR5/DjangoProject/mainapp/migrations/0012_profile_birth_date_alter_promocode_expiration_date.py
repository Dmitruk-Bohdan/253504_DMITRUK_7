# Generated by Django 5.0.4 on 2024-05-10 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_remove_profile_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 9, 17, 46, 4, 303020)),
        ),
    ]
