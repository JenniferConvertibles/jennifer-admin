# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-21 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20161021_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='position',
            field=models.IntegerField(default=1),
        ),
    ]