# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-22 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20191222_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False),
        ),
    ]
