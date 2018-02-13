#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from app01 import views

urlpatterns = [
    url(r'test/', views.test),
]