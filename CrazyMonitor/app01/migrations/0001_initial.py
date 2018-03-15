# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-15 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('conditions', models.TextField()),
                ('interval', models.IntegerField(default=300)),
                ('recover_notics', models.BooleanField(default=True)),
                ('recover_subject', models.CharField(blank=True, max_length=128, null=True)),
                ('recover_message', models.TextField(default=True)),
                ('enable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActionOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('step', models.SmallIntegerField(default=1)),
                ('action_type', models.CharField(choices=[('email', 'Email'), ('sms', 'SMS'), ('script', 'RunScript')], default='email', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
                ('monitored_by', models.CharField(choices=[('agent', 'Agent'), ('snmp', 'SNMP'), ('wget', 'WGET')], max_length=65)),
                ('status', models.IntegerField(choices=[(1, 'Online'), (2, 'Down'), (3, 'Unreachable'), (1, 'Offline')], default=1)),
                ('memo', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('memo', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('content', models.TextField(verbose_name='维护内容')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('host', models.ManyToManyField(blank=True, to='app01.Host')),
                ('host_group', models.ManyToManyField(blank=True, to='app01.HostGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('interval', models.IntegerField(default=60)),
                ('plugin_name', models.CharField(default='n/a', max_length=64)),
                ('memo', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('key', models.CharField(max_length=64)),
                ('data_type', models.CharField(choices=[('int', 'int'), ('float', 'float'), ('str', 'string')], max_length=64)),
                ('memo', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('services', models.ManyToManyField(to='app01.Service', verbose_name='服务列表')),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('serverity', models.IntegerField(choices=[(1, 'Information'), (2, 'Warning'), (1, 'Average'), (1, 'Hight'), (1, 'Diaster')])),
                ('enable', models.BooleanField(default=True)),
                ('memo', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TriggerExpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specified_index_key', models.CharField(max_length=32, verbose_name='只监控专门指定的')),
                ('data_clac_func', models.CharField(choices=[('avg', 'Average'), ('max', 'Max'), ('hit', 'Hit'), ('avg', 'Average'), ('last', 'Last')], max_length=32)),
                ('data_clac_args', models.CharField(help_text='若是多个参数，用,号分开。', max_length=64)),
                ('threshold', models.IntegerField(verbose_name='阀值')),
                ('operator_type', models.CharField(choices=[('eq', '='), ('lt', '<'), ('gt', '>')], max_length=32, verbose_name='运算符')),
                ('logic_type', models.CharField(choices=[('or', 'OR'), ('and', 'AND')], max_length=64)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Service', verbose_name='关联的服务名')),
                ('service_index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.ServiceIndex', verbose_name='关联的服务指标')),
                ('trigger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Trigger', verbose_name='所属触发器')),
            ],
        ),
        migrations.AddField(
            model_name='template',
            name='trigger',
            field=models.ManyToManyField(to='app01.Trigger', verbose_name='触发器列表'),
        ),
        migrations.AddField(
            model_name='service',
            name='items',
            field=models.ManyToManyField(blank=True, to='app01.ServiceIndex', verbose_name='指标列表'),
        ),
        migrations.AddField(
            model_name='hostgroup',
            name='templates',
            field=models.ManyToManyField(blank=True, to='app01.Template'),
        ),
        migrations.AddField(
            model_name='host',
            name='host_group',
            field=models.ManyToManyField(blank=True, to='app01.HostGroup'),
        ),
        migrations.AddField(
            model_name='host',
            name='templates',
            field=models.ManyToManyField(blank=True, to='app01.Template'),
        ),
        migrations.AddField(
            model_name='action',
            name='host',
            field=models.ManyToManyField(blank=True, to='app01.Host'),
        ),
        migrations.AddField(
            model_name='action',
            name='host_group',
            field=models.ManyToManyField(blank=True, to='app01.HostGroup'),
        ),
        migrations.AddField(
            model_name='action',
            name='operations',
            field=models.ManyToManyField(to='app01.ActionOperation'),
        ),
    ]
