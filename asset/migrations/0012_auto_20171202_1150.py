# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-02 08:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0011_auto_20171202_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('removed', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('description', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='id_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.IdType'),
        ),
    ]
