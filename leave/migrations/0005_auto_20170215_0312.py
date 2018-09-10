# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-15 00:12
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import leave.models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0004_auto_20170214_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavetype',
            name='pay_percentage',
            field=models.DecimalField(decimal_places=1, default=Decimal('100'), max_digits=4),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='positions',
            field=models.ManyToManyField(default=leave.models.all_positions, to='payroll.Position'),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='service_lines',
            field=models.ManyToManyField(default=leave.models.all_service_lines, to='payroll.ServiceLine'),
        ),
    ]
