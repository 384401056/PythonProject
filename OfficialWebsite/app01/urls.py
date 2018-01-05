#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
import app01

urlpatterns = [
    url(r'^', include('app01.urls')),
]
