# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-04 02:10
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models
import stdimage.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0002_auto_20180220_1503'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish', models.BooleanField(db_index=True, default=True, verbose_name='Публикация')),
                ('name', models.CharField(max_length=140, verbose_name='Имя')),
                ('address', models.CharField(blank=True, max_length=140, verbose_name='Адрес')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('site', models.CharField(blank=True, max_length=50, verbose_name='Сайт')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание')),
                ('avatar', stdimage.models.StdImageField(upload_to=stdimage.utils.UploadToUUID(path='images'))),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish', models.BooleanField(db_index=True, default=True, verbose_name='Публикация')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Город')),
                ('slug', models.SlugField(blank=True, max_length=140, null=True)),
            ],
            options={
                'verbose_name': 'Место проведения',
                'verbose_name_plural': 'Места проведения',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish', models.BooleanField(db_index=True, default=True, verbose_name='Публикация')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Стоимость')),
                ('slug', models.SlugField(blank=True, max_length=140, null=True)),
            ],
            options={
                'verbose_name': 'Стоимость',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='TypeCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish', models.BooleanField(db_index=True, default=True, verbose_name='Публикация')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Тип компании')),
                ('slug', models.SlugField(blank=True, max_length=140, null=True)),
            ],
            options={
                'verbose_name': 'Тип компании',
                'verbose_name_plural': 'Типы компании',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='company',
            name='locations',
            field=models.ManyToManyField(blank=True, to='company.Location', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='company',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Price', verbose_name='Стоимость'),
        ),
        migrations.AddField(
            model_name='company',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag', verbose_name='Тэги'),
        ),
        migrations.AddField(
            model_name='company',
            name='type',
            field=models.ManyToManyField(to='company.TypeCompany', verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
