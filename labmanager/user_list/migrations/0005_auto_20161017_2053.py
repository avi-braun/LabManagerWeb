# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-17 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0004_auto_20161005_0006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('user_rank', 'name')},
        ),
        migrations.AddField(
            model_name='user',
            name='user_rank',
            field=models.CharField(choices=[('BSc', 'Under graduate'), ('MSc', 'MSC student'), ('PhD', 'PhD student'), ('Staff', 'Academic staff')], default='Academic staff', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('A', 'Lab admin'), ('S', 'User'), ('N', 'Non Active')], max_length=1),
        ),
    ]
