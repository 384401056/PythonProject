#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Blueice'
__date__ = '2018/6/12 18:03'

import xadmin
from xadmin import views
from Apps.User.models import EmailVerifyRecord, Banner


class BaseSetting(object):
    '''
    xadmin全局配置
    '''
    enable_themes = True  # 开启主题
    use_bootswatch = True

class GlobalSetting(object):
    site_title = "慕学在线后台管理系统"
    site_footer = "慕学在线教育平台"
    # menu_style = "accordion"

class EmailVerifyRecordAdmin(object):
    list_display = ["code","email","send_type","send_time"]
    search_fields = ["code","email","send_type"]
    list_filter = ["code","email","send_type","send_time"]

class BannerAdmin(object):
    list_display = ["title", "image", "url", "index","add_time"]
    search_fields = ["title", "image", "url", "index"]
    list_filter = ["title", "image", "url", "index","add_time"]

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting) # 注册基础配置类
xadmin.site.register(views.CommAdminView, GlobalSetting) # 注册全局配置类