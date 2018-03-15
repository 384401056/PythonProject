#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import os

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.21.134',22, 'root', '123456')
stdin, stdout, stderr = ssh.exec_command('ifconfig')
print(stdout.read())
ssh.close()
