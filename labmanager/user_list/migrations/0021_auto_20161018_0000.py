# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-17 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0020_auto_20161017_2313'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('users', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('NA', 'Non Active'), ('Active', 'Active')], default='Active', max_length=8),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_rank',
            field=models.CharField(choices=[('BSc', 'Under graduate'), ('MSc', 'MSC student'), ('PhD', 'PhD student'), ('Staff', 'Staff'), ('Other', 'Other')], default='Other', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('U', 'User'), ('A', 'Lab admin')], default='Non Active', max_length=10),
        ),
    ]
