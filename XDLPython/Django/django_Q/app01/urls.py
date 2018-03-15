#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.index),  # 指定路由.
    url(r'^django', views.django),  # 指定路由.
]
