# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-05 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_room', '0005_auto_20170104_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='icon',
            field=models.CharField(max_length=255, null=True, verbose_name='Icona Classe'),
        ),
    ]