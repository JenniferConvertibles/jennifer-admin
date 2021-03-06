# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-31 15:20
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20161028_1121'),
        ('schedule', '0008_auto_20161028_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='change',
            name='compare_at_price',
        ),
        migrations.RemoveField(
            model_name='change',
            name='price',
        ),
        migrations.RemoveField(
            model_name='change',
            name='sale_price',
        ),
        migrations.RemoveField(
            model_name='change',
            name='variant',
        ),
        migrations.AddField(
            model_name='change',
            name='json',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='change',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='changes', to='products.Product'),
            preserve_default=False,
        ),
    ]
