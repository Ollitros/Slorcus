# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Library', '0007_auto_20171023_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('quantity', models.CharField(max_length=4096)),
                ('mobile_number', models.EmailField(max_length=32)),
                ('appendage', models.TextField(max_length=2048)),
                ('total_price', models.CharField(max_length=256)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Book')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=1024)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Book')),
            ],
            options={
                'verbose_name': 'OrderInBasket',
                'verbose_name_plural': 'OrdersInBasket',
            },
        ),
    ]