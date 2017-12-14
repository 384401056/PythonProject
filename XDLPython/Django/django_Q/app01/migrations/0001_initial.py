# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-06 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('page', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pubdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.BookType'),
        ),
    ]