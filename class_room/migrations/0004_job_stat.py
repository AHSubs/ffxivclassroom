# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-04 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class_room', '0003_auto_20170104_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='stat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='class_room.Stat', verbose_name='Statistica Primaria'),
        ),
    ]