#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from app01 import views

urlpatterns = [

    # 客户端调用接口
    url(r'client/config/(\d+)/$', views.client_configs),
    url(r'service/report/$', views.server_data_report),

    # 前端调用接口
    url(r'getAllHostGroup/', views.get_all_hostgroup),
    url(r'getHostsByGroupId/(\d+)/$', views.get_host_by_groupid),
    url(r'getRealDataByHostId/(\d+)/$', views.get_real_data_by_hostid),
    url(r'getAllDataByHostId/(\d+)/$', views.get_all_data_by_hostid),


    # 测试接口
    url(r'test/', views.test),
]
