# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0042_auto_20170525_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='removed',
            field=models.DateTimeField(blank=True, default=None, editable=False, null=True),
        ),
    ]
