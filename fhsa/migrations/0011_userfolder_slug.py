# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 20:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fhsa', '0010_auto_20160229_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfolder',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 3, 2, 20, 27, 30, 972159, tzinfo=utc)),
            preserve_default=False,
        ),
    ]