# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-17 22:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0017_auto_20161017_2302'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]