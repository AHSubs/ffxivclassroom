# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-04 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lore', models.TextField(blank=True, verbose_name='Lore')),
                ('icon', models.CharField(max_length=255, null=True, verbose_name='Icona Classe / Job')),
                ('creat_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data di Creazione')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Data di Pubblicazione')),
            ],
            options={
                'verbose_name_plural': 'Classi Base',
                'verbose_name': 'Classe Base',
            },
        ),
        migrations.CreateModel(
            name='BaseClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseclassname', models.CharField(choices=[('Gladiator', 'GLA'), ('Marauder', 'MRD'), ('Pugilist', 'PGL'), ('Lancer', 'LNC'), ('Archer', 'ARC'), ('Rogue', 'ROG'), ('Conjurer', 'CNJ'), ('Thaumaturge', 'THM'), ('Arcanist', 'ACN'), ('Nessuno', '-')], max_length=40, verbose_name='Elenco Classi Base')),
            ],
            options={
                'verbose_name_plural': 'Classi (Base)',
                'verbose_name': 'Classe (Base)',
            },
        ),
        migrations.CreateModel(
            name='BaseJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basejobname', models.CharField(choices=[('Paladin', 'PLD'), ('Warrior', 'WAR'), ('Dark Knight', 'DRK'), ('Monk', 'MNK'), ('Dragoon', 'DRG'), ('Bard', 'BRD'), ('Machinist', 'MCH'), ('Ninja', 'NIN'), ('White Mage', 'WHM'), ('Black Mage', 'BLM'), ('Scholar', 'SCH'), ('Summoner', 'SMN'), ('Astrologian', 'AST')], max_length=40, verbose_name='Elenco Job')),
            ],
            options={
                'verbose_name_plural': 'FFXIV JOBS',
                'verbose_name': 'FFXIVJob',
            },
        ),
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expname', models.CharField(choices=[('A Realm Reborn', 'ARR'), ('Heavensward', 'HW')], max_length=20, verbose_name='Espansione Di Uscita')),
            ],
            options={
                'verbose_name_plural': 'Espansioni',
                'verbose_name': 'Espansione',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lore', models.TextField(blank=True, verbose_name='Lore JOB')),
                ('icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='Icona JOB')),
                ('creat_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data di Creazione')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Data di Pubblicazione')),
                ('avail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.Expansion', verbose_name='Espansione di Uscita')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.BaseJob', verbose_name='Nome Job')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
                'verbose_name': 'Job',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvllist', models.CharField(choices=[('15', '15'), ('30', '30'), ('-', '-')], max_length=2, verbose_name='Livello')),
            ],
            options={
                'verbose_name_plural': 'Livelli',
                'verbose_name': 'Livello',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(choices=[('TANK', 'Tank'), ('DPS', 'Dps'), ('HEALER', 'Healer')], max_length=10, verbose_name='Nome Ruolo')),
            ],
            options={
                'verbose_name_plural': 'Ruolo',
                'verbose_name': 'Ruolo',
            },
        ),
        migrations.AddField(
            model_name='job',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.Role', verbose_name='Ruolo'),
        ),
        migrations.AddField(
            model_name='job',
            name='transfrom1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfrom1', to='class_room.BaseClass', verbose_name='Nome Classe 1'),
        ),
        migrations.AddField(
            model_name='job',
            name='transfrom2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfrom2', to='class_room.BaseClass', verbose_name='Nome Classe 2'),
        ),
        migrations.AddField(
            model_name='job',
            name='transfromlvl1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfromlvl1', to='class_room.Level', verbose_name='Livello 1'),
        ),
        migrations.AddField(
            model_name='job',
            name='transfromlvl2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfromlvl2', to='class_room.Level', verbose_name='Livello 2'),
        ),
        migrations.AddField(
            model_name='base',
            name='avail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.Expansion', verbose_name='Espansione di Uscita'),
        ),
        migrations.AddField(
            model_name='base',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.BaseClass', verbose_name='Nome Classe'),
        ),
        migrations.AddField(
            model_name='base',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.Role', verbose_name='Ruolo'),
        ),
        migrations.AddField(
            model_name='base',
            name='transformin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.BaseJob', verbose_name='Trasformazione in Job'),
        ),
        migrations.AddField(
            model_name='base',
            name='trasforminjobat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.Level', verbose_name='Trasformazione in Job al livello'),
        ),
    ]
