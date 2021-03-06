# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-12 14:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models
import stdimage.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_auto_20181003_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish', models.BooleanField(db_index=True, default=True, verbose_name='Publish')),
                ('name', models.CharField(default='Portfolio', max_length=70, verbose_name='Name')),
                ('summary', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Company')),
            ],
            options={
                'verbose_name_plural': 'Albums',
                'verbose_name': 'Album',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish', models.BooleanField(db_index=True, default=True, verbose_name='Publish')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Name')),
                ('image', stdimage.models.StdImageField(upload_to=stdimage.utils.UploadToUUID(path='photos'), verbose_name='Image')),
                ('is_cover_photo', models.BooleanField(verbose_name='Is cover photo ')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Фотографії',
                'verbose_name': 'Photo',
            },
        ),
    ]
