# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-14 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20170513_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.TextField(null=True),
        ),
    ]
