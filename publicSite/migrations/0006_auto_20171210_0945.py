# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicSite', '0005_auto_20171210_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='dollars',
            new_name='actual_dollars',
        ),
    ]