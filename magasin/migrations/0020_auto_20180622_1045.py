# Generated by Django 2.0.6 on 2018-06-22 08:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0019_auto_20180619_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 22, 8, 45, 41, 362149, tzinfo=utc)),
        ),
    ]
