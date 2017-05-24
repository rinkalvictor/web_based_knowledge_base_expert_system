# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-08 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0007_auto_20170504_1357'),
        ('comments', '0003_comment_confidence_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_first', models.BooleanField(default=False)),
                ('is_last', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
                ('response', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='response', to='comments.Comment')),
                ('solution', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='comments.Comment')),
            ],
        ),
    ]