# Generated by Django 4.1.13 on 2023-12-22 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 22, 9, 41, 12, 15492)),
        ),
    ]
