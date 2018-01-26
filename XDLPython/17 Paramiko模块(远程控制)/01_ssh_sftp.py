#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import os


import paramiko
import os

t = paramiko.Transport(('118.190.43.87', 22))
t.connect(username='root', password='Flzxl9t!')

sftp = paramiko.SFTPClient.from_transport(t)

# 上传文件,指明源文件路径，及目标路径文件名。
sftp.put('/home/gyb/python_pro/Paramiko/111.txt', '/home/coap/111.txt')

# 下载文件, 先指定源文件路径，然后才是目标文件
# sftp.get('/home/coap/nodejsCoap/server.js', '/home/gyb/python_pro/Paramiko/server.js')

t.close()


