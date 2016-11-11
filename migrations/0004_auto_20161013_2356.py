# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 05:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('swiing', '0003_adventure_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventure',
            name='short_description',
            field=models.CharField(default=datetime.datetime(2016, 10, 14, 5, 56, 31, 219064, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adventure',
            name='unique_title',
            field=models.CharField(default=datetime.datetime(2016, 10, 14, 5, 56, 41, 843139, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
