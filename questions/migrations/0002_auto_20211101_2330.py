# Generated by Django 3.1.3 on 2021-11-01 23:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 23, 24, 26, 28623, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 23, 24, 26, 28570, tzinfo=utc)),
        ),
    ]