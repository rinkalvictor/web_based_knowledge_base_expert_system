# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-14 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170504_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.TextField(default=False),
        ),
    ]
