# Generated by Django 5.0.4 on 2024-09-18 11:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0045_alter_promocode_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='promocode',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.promocode'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 18, 14, 28, 12, 335250)),
        ),
    ]
