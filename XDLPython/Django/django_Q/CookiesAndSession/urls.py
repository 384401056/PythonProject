#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.index),  # 指定路由.
    url(r'^cook1/', views.cook1),  # 指定路由.
    url(r'^cook2/', views.cook2),  # 指定路由.
    url(r'^session/', views.session),  # 指定路由.
]
