#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 需要pip install celery
# 需要pip install celery-with-redis
from celery import Celery
import subprocess

broker = 'redis://127.0.0.1'
backend = 'redis://127.0.0.1'

# task与文件名相同
app = Celery('task', broker=broker, backend=backend)


@app.task
def add(x, y):
    print('add......', x, y)
    return x+y

def run_cmd(cmd):
    cmd_obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



# 在cmd中进入本文件的目录,进行python的执行环境下。
# r = add.delay(5, 7)
# add.delay(5, 7)

# 其中r可以保存返回结果
# r.get()