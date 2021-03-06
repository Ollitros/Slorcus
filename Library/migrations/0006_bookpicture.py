# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0005_auto_20171021_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='book_images/')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Library.Book')),
            ],
        ),
    ]
