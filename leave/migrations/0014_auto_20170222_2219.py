# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-22 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0013_auto_20170217_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplicationreview',
            name='leave_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('D', 'Denied'), ('C', 'Canceled'), ('E', 'Expired')], default='P', max_length=2),
        ),
    ]
