# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_auto_20161126_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.IntegerField(choices=[(0, 'Prepared'), (1, 'Confirmed'), (2, 'Canceled')]),
        ),
    ]
