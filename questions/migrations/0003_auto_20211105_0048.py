# Generated by Django 3.1.3 on 2021-11-05 00:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20211101_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 0, 48, 34, 978462, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 0, 48, 34, 978435, tzinfo=utc)),
        ),
    ]
