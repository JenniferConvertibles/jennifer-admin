# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_variant_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='shopify_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]