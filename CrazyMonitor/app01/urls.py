#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from app01 import views

urlpatterns = [
    url(r'index/', views.index),
    url(r'api/client/config/(\d+)/$', views.client_configs),
    url(r'api/service/report/$', views.server_data_report),
]