#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Blueice'
__date__ = '2018/6/20 14:17'


import os
from datetime import datetime
from MxOnline import settings


# Create your models here.


def upload_to(instance, filename):
    '''
    让上传的文件路径动态地与model的名字有关
    :param instance: 使用这处upload_to函数的model。
    :param filename: 上传的文件名。
    :return:
    '''
    className = str(type(instance))[:-2].split('.')[-1] # 类名
    nowTime = datetime.now().strftime('%Y-%m-%d')  # 时间
    # return os.path.join(settings.MEDIA_ROOT, className, str(instance), nowTime, filename)
    return '/'.join([className, str(instance), nowTime, filename])

