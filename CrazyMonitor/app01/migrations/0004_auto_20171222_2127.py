# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-22 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20171221_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triggerexpression',
            name='logic_type',
            field=models.CharField(blank=True, choices=[('or', 'OR'), ('and', 'AND')], max_length=64),
        ),
    ]