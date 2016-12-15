# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('rating', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('picture0', models.CharField(max_length=1000)),
                ('picture1', models.CharField(max_length=1000)),
                ('picture2', models.CharField(max_length=1000)),
                ('picture3', models.CharField(max_length=1000)),
                ('picture4', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('rating', models.CharField(max_length=250)),
                ('thumbnail', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]
