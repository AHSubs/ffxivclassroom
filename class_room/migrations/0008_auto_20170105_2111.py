# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-05 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_room', '0007_auto_20170105_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='portait',
            field=models.CharField(max_length=255, null=True, verbose_name='Immagine'),
        ),
        migrations.AddField(
            model_name='job',
            name='portait',
            field=models.CharField(max_length=255, null=True, verbose_name='Immagine Job'),
        ),
    ]
