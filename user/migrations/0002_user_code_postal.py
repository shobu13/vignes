# Generated by Django 2.0.6 on 2018-06-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code_postal',
            field=models.CharField(default='', max_length=5),
        ),
    ]
