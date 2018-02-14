#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from app01 import views

urlpatterns = [
    # 前端调用接口
    url(r'getAllHostGroup/', views.get_all_hostgroup),
    url(r'getHostsByGroupId/(\d+)/$', views.get_hosts_by_groupid),
    url(r'getRealDataByHostId/(\d+)/$', views.get_real_data_by_hostid),
    url(r'getRealLastestDataByHostId/(\d+)/(\w+)/(\w+)/$', views.get_redis_latest_data_by_hostid),
    url(r'getAllDataByHostId/(\d+)/$', views.get_all_data_by_hostid),

    # 测试接口
    url(r'test/', views.test),
]