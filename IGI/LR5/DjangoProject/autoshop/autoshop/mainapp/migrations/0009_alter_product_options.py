# Generated by Django 5.0.4 on 2024-05-05 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_vacancy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
    ]
