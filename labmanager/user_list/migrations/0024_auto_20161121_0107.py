# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-21 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0023_auto_20161120_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='CID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]