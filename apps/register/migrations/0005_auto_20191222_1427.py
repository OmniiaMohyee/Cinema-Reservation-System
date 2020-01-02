# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-22 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20191222_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='screeing_seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_time_id', models.IntegerField(default=0)),
                ('row', models.IntegerField(default=0)),
                ('column', models.IntegerField(default=0)),
                ('taken', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ScreenManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Genre',
            new_name='genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='screen_number',
        ),
        migrations.RemoveField(
            model_name='movie_screentime',
            name='id',
        ),
        migrations.AddField(
            model_name='movie_screentime',
            name='screen_time_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]