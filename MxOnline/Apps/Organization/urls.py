#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Blueice'
__date__ = '2018/6/21 10:31'


from django.urls import path, re_path, include
from django.views.generic import TemplateView
from Apps.Organization.views import *

# 在Django2.0中，使用app_name的形式来定义url的namespace
app_name='org'

urlpatterns = [
    path(r'list/', OrgListView.as_view(), name="org_list"),
    path(r'add_ask/', AddUserAskView.as_view(), name="add_ask"),
    path(r'home/<int:org_id>', OrgHome.as_view(), name="home"),
    path(r'course/<int:org_id>', OrgCourse.as_view(), name="course"),
    path(r'desc/<int:org_id>', OrgDesc.as_view(), name="desc"),
    path(r'teachers/<int:org_id>', OrgTeacher.as_view(), name="teachers"),
]