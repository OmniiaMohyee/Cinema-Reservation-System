# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-23 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20191222_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screeing_seats',
            old_name='column',
            new_name='seat_number',
        ),
        migrations.RemoveField(
            model_name='screeing_seats',
            name='row',
        ),
    ]
