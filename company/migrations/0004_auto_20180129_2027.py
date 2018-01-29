# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-29 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20180123_0850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name'], 'verbose_name': 'Место проведения', 'verbose_name_plural': 'Места проведения'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Стоимость', 'verbose_name_plural': 'Цены'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.AlterModelOptions(
            name='typecompany',
            options={'ordering': ['name'], 'verbose_name': 'Тип компании', 'verbose_name_plural': 'Типы компании'},
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=140, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='company',
            name='img',
            field=models.ImageField(upload_to='img', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='company',
            name='locations',
            field=models.ManyToManyField(blank=True, to='company.Location', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=140, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='company',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Price', verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='company',
            name='site',
            field=models.CharField(blank=True, max_length=50, verbose_name='Сайт'),
        ),
        migrations.AlterField(
            model_name='company',
            name='tags',
            field=models.ManyToManyField(blank=True, to='company.Tag', verbose_name='Тэги'),
        ),
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.ManyToManyField(to='company.TypeCompany', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='price',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Имя тэга'),
        ),
        migrations.AlterField(
            model_name='typecompany',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Тип компании'),
        ),
    ]