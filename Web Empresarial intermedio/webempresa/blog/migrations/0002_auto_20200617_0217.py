# Generated by Django 2.0.2 on 2020-06-17 02:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 2, 17, 38, 113941, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
