# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-15 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bags', '0003_auto_20170613_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='thumbnail',
            field=models.URLField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='photos',
            name='photo_url',
            field=models.URLField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.URLField(default='', max_length=500),
        ),
    ]