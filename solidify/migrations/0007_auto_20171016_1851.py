# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 09:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solidify', '0006_auto_20171016_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objinput',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 16, 18, 51, 40, 732267)),
        ),
    ]
