# Generated by Django 5.0.4 on 2024-05-13 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_rename_date_review_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 12, 16, 19, 31, 168570)),
        ),
    ]
