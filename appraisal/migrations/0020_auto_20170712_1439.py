# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-12 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal', '0019_auto_20170712_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeappraisalflow',
            old_name='reviewer',
            new_name='to_reviewer',
        ),
    ]
