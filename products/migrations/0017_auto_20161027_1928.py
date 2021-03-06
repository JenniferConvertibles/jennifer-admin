# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-27 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_product_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='code',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.ProductType'),
        ),
        migrations.AlterField(
            model_name='product',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='series.Series'),
        ),
    ]
