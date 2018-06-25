from django.shortcuts import render, HttpResponse
from django.views.generic.base import View

import json
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Course
from Apps.Operation.models import UserFavorite


# Create your views here.

class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all().order_by("-add_time")  # 默认按时间倒序排列。
        hot_courses = courses.order_by("-click_num")[:3]  # 热门学习推荐

        try:
            page = request.GET.get("page", 1)  # 获取页码，默认为1
        except PageNotAnInteger:
            page = 1

        sort = request.GET.get('sort', "")
        if sort:
            order_str = "-" + sort  #
            courses = courses.order_by(order_str)

        # 创建分页对象。每页6个
        p = Paginator(courses, request=request, per_page=6)

        ret = {
            "sort": sort,
            "hot_courses": hot_courses,
            "courses": p.page(page),  # 返回分页数据
            "current_page": "course",
        }
        return render(request, "course-list.html", ret)


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)

        # 课程点击数加1
        course.click_num += 1
        course.save()

        relate_course = [] # 相关课程列表
        if course.tag:
            # 通过标签字段，获取本课程的相关课程列表。先排除自己exclude(id=course_id)，再找相关课程.
            relate_course = Course.objects.exclude(id=course_id).filter(tag__contains=course.tag)[:3]

        has_fav_course = False # 是否收藏过此课程
        has_fav_org = False # 是否收藏过此机构

        # 判断用户是否收藏过本页的课程和机构。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        ret = {
            "course": course,
            "relate_course": relate_course,
            "current_page": "course",
            "has_fav_course":has_fav_course,
            "has_fav_org":has_fav_org,
        }
        return render(request, "course-detail.html", ret)
