#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import Celery

broker = 'redis://127.0.0.1'
backend = 'redis://127.0.0.1'

app = Celery('proj',
             broker=broker,
             backend=backend,
             include=['my_proj.tasks'],
             )

app.conf.update(
    result_expires = 3600,
)

if __name__ =='__main__':
    app.start()
