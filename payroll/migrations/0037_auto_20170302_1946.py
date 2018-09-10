# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-02 16:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0036_auto_20170302_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeeprofile',
            options={'ordering': ['user__last_name'], 'permissions': (('hrp_configure_company', 'Can edit company Info (Configure -> Positions/Service Lines, ...)'), ('hrp_configure_pim', 'Can configure Personnel Info'), ('hrp_manage_employee_info', 'Can manage employees (PIM -> Employees -> Add/Update)'), ('hrp_configure_leave', 'Can configure Leave Info (Leave -> Setup)'), ('hrp_handle_leave_requests', 'Can authorize leave days (Leave -> Applications -> Received)'), ('hrp_configure_payroll', 'Can configure Payroll Info (Payroll -> Setup)'), ('hrp_manage_payroll', 'Can generate/edit payroll (Payroll -> Payroll Cycles -> Add)'))},
        ),
    ]
