# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=100)),
                ('scene_count', models.IntegerField()),
                ('pixel_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_start', models.DateTimeField(verbose_name='query_start')),
                ('query_end', models.DateTimeField(verbose_name='query_end')),
                ('user_id', models.CharField(max_length=25)),
                ('query_type', models.CharField(max_length=25)),
                ('upper_lat', models.FloatField()),
                ('lower_lat', models.FloatField()),
                ('upper_long', models.FloatField()),
                ('lower_long', models.FloatField()),
                ('time_start', models.DateTimeField(verbose_name='time_start')),
                ('time_end', models.DateTimeField(verbose_name='time_end')),
                ('platform', models.CharField(max_length=25)),
                ('product', models.CharField(max_length=25)),
                ('product_type', models.CharField(max_length=25)),
                ('measurements', models.CharField(max_length=100)),
                ('query_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=100)),
                ('result_path', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SatelliteBands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satellite_name', models.CharField(max_length=25)),
                ('platform', models.CharField(max_length=25)),
                ('available_bands', models.CharField(max_length=100)),
            ],
        ),
    ]
