#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Blueice'
__date__ = '2018/6/21 10:31'


from django.urls import path, re_path, include
from django.views.generic import TemplateView
from Apps.Courses.views import *

# 在Django2.0中，使用app_name的形式来定义url的namespace
app_name='course'

urlpatterns = [
    path(r'list/', CourseListView.as_view(), name="course_list"),
    path(r'detail/<int:course_id>', CourseDetailView.as_view(), name="course_detail"),
]