# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20171007_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='hotel_id',
            new_name='hotel',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
