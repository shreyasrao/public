# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysong',
            name='img_url',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mysong',
            name='song_url',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='song',
            name='img_url',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_url',
            field=models.CharField(max_length=500),
        ),
    ]
