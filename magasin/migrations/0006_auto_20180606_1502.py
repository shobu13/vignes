# Generated by Django 2.0.3 on 2018-06-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0005_auto_20180605_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
