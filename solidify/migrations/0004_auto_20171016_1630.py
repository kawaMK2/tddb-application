# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 07:30
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solidify', '0003_auto_20171016_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objinput',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 16, 16, 30, 7, 156701)),
        ),
        migrations.AlterField(
            model_name='objinput',
            name='b',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)]),
        ),
        migrations.AlterField(
            model_name='objinput',
            name='g',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)]),
        ),
        migrations.AlterField(
            model_name='objinput',
            name='r',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)]),
        ),
    ]
