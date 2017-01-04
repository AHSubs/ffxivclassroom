# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-04 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class_room', '0002_auto_20170104_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statsname', models.CharField(choices=[('Vitality', 'VIT'), ('Strength', 'STR'), ('Dexterity', 'DEX'), ('Intelligence', 'INT'), ('Mind', 'Mind'), ('Piety', 'PIE')], max_length=30, verbose_name='Nome Statistica')),
            ],
            options={
                'verbose_name_plural': 'Statistiche',
                'verbose_name': 'Statistica',
            },
        ),
        migrations.AddField(
            model_name='base',
            name='stat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='class_room.Stat', verbose_name='Statistica Primaria'),
        ),
    ]
