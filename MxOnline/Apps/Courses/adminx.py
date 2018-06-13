#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Blueice'
__date__ = '2018/6/13 10:20'

from Apps.Courses.models import Course, Lesson, Video, CourseResource
import xadmin

class CourseAdmin(object):
    list_display = ["name", "desc", "degree", "learn_times","students","fav_nums","click_num", "add_time"]
    search_fields = ["name", "desc", "degree", "learn_times","students","fav_nums","click_num"]
    list_filter = ["name", "desc", "degree", "learn_times","students","fav_nums","click_num", "add_time"]

class LessonAdmin(object):
    list_display = ["course","name","add_time"]
    search_fields = ["course","name"]
    list_filter = ["course__name","name","add_time"] # course是外键，所以要指明过滤的字段

class VideoAdmin(object):
    list_display = ["lesson", "name", "add_time"]
    search_fields = ["lesson", "name"]
    list_filter = ["lesson__name", "name", "add_time"]

class CourseResourceAdmin(object):
    list_display = ["course", "name", "download","add_time"]
    search_fields = ["course", "name", "download"]
    list_filter = ["course__name", "name", "download","add_time"]

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)