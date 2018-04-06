#!/usr/bin/env python
# -*- coding: utf-8 -*-

from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

#pip install celery-with-redis
broker = 'redis://127.0.0.1'
backend = 'redis://127.0.0.1'

app = Celery('taskApp', broker=broker, backend=backend)

# 使用配置文件的形式。
app.conf.update(
    CELERY_TIMEZONE = 'Asia/Shanghai', # 设置时区.
    CELERYBEAT_SCHEDULE={
        'add': {
            'task': 'tasks.add',
            'schedule': crontab(minute='43',hour='17'),
            'args': (11, 22)
        }
    },
)



@app.task
def add(x, y):
    print(x + y)