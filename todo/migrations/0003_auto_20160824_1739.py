# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20160824_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_resolved',
            field=models.BooleanField(default=False, verbose_name='Resolved?'),
        ),
    ]
