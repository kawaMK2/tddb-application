# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 08:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solidify', '0004_auto_20171016_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='objinput',
            name='height',
            field=models.FloatField(default=1.0, max_length=100.0),
        ),
        migrations.AlterField(
            model_name='objinput',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 16, 17, 24, 27, 127626)),
        ),
        migrations.AlterField(
            model_name='objinput',
            name='name',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
