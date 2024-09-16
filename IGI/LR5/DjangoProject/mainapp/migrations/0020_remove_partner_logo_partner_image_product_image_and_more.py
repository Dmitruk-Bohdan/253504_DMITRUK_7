# Generated by Django 5.0.4 on 2024-09-16 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_partner_alter_promocode_expiration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='logo',
        ),
        migrations.AddField(
            model_name='partner',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/partners_logos/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/products/'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='website',
            field=models.URLField(default='https://minsk-lada.by'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 16, 14, 21, 18, 184889)),
        ),
    ]
