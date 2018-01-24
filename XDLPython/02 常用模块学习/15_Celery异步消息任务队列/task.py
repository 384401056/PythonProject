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

@app.task
def prin(cmd):
    print(cmd)
    return 0

@app.task
def run_cmd(cmd):
    # 执行系统命令，返回执行结果(bytes类型)
    ret = subprocess.check_output(cmd)
    # print(str(ret, encoding='gbk')) # 直接输出gbk字符串
    ret_byte = ret.decode('gbk').encode('utf-8')  # 将返字符从gbk转成utf-8字节
    ret_utf8 = str(ret_byte, encoding='utf-8')  # 将字节转为utf-8字符串
    return ret_utf8

# 1.在cmd中运行,其中task是py文件名.
# celery -A task worker --loglevel=info
# 可启动多个任务队列
# celery multi start w1 -a task worker --loglevel=info
# 2.在新cmd中进入本文件的目录,进行python的执行环境下。
# import task
# r = task.add.delay(5, 7)
# r.get()
# 其中r可以保存返回结果
