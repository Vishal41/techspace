# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-05 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_clubs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clubs',
            new_name='Club',
        ),
    ]