#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Blueice'
__date__ = '2018/6/12 18:03'

import xadmin
from .models import EmailVerifyRecord, Banner

class EmailVerifyRecordAdmin(object):
    pass

class BannerAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)