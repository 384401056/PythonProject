#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from app01 import views

urlpatterns = [
    url(r'get_user/', views.get_user),
    url(r'test/', views.test),
]