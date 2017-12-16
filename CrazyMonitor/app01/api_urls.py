#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from app01 import views

urlpatterns = [
    url(r'index/', views.index),
    url(r'client/config/(\d+)/$', views.client_configs),
    url(r'service/report/$', views.server_data_report),
]