# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-22 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20171222_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
    ]