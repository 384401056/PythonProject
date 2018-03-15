#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 需要pip install celery
# 需要pip install celery-with-redis
import sys
sys.path.append('/home/gyb/python_pro/my_proj')
from .celery import app

@app.task
def add(x, y):
    return x+y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)