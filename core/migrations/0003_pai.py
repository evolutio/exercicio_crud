# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-28 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('countfilhos', models.IntegerField()),
                ('maisvelho', models.CharField(max_length=128)),
            ],
        ),
    ]