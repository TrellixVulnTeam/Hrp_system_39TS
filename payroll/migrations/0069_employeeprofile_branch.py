# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-07 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0068_auto_20180907_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payroll.Branch'),
        ),
    ]
