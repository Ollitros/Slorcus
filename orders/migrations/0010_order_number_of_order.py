# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20171118_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='number_of_order',
            field=models.CharField(max_length=4096, null=True),
        ),
    ]
