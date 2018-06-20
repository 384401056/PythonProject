#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Blueice'
__date__ = '2018/6/13 10:38'

import xadmin

from Apps.Organization.models import *

class CityDictAdmin(object):
    list_display = ["name", "desc", "add_time"]
    search_fields = ["name", "desc"]
    list_filter = ["name", "desc", "add_time"]

class CourseOrgAdmin(object):
    list_display = ["name", "desc", "city","address","fav_nums","click_num","category","add_time"]
    search_fields = ["name", "desc", "city","address","fav_nums","category","click_num"]
    list_filter = ["name", "desc", "city","address","fav_nums","click_num","category","add_time"]

class TeacherAdmin(object):
    list_display = ["name", "org", "work_years","work_company","work_position","points","fav_nums","add_time"]
    search_fields = ["name", "org", "work_years","work_company","work_position","points","fav_nums"]
    list_filter = ["name", "org", "work_years","work_company","work_position","points","fav_nums","add_time"]

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)