# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-19 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_album_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='publish',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Publish'),
        ),
    ]
