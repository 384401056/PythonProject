from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic.base import View
import json
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from MxOnline import settings
from .form import UserAskForm


# Create your views here.



class OrgListView(View):
    '''
    课程机构列表
    '''

    def get(self, request):
        ret = {}
        orgs = CourseOrg.objects.all()  # 机构列表
        hot_orgs = orgs.order_by("-click_num")[:4]  # 在机构中通过排序，找出前4家点击量最高的机构，做为执门机构

        try:
            page = request.GET.get("page", 1)  # 获取页码，默认为1
        except PageNotAnInteger:
            page = 1

        # 接收查询参数
        city_id = request.GET.get('city', "")
        ct = request.GET.get('ct', "")
        sort = request.GET.get('sort', "")

        if city_id:
            orgs = orgs.filter(city_id=int(city_id))  # 筛选出选中城市的机构,这里要把str转为int

        if ct:
            orgs = orgs.filter(category=ct)  # 筛选出选中类型的机构

        if sort:
            order_str = "-" + sort
            orgs = orgs.order_by(order_str)

        # 创建分页对象。
        p = Paginator(orgs, request=request, per_page=4)  # per_page每页数
        # per_page = settings.PAGINATION_SETTINGS['PAGE_RANGE_DISPLAYED'] # 每页数

        # 返回值组装
        ret = {
            'city_id': city_id,  # 根据返回的city_id改变a标签的样式
            'ct': ct,  # 根据返回的ct改变a标签的样式
            'sort': sort,

            'org_num': orgs.count(),  # 机构数量

            'cities': CityDict.objects.all(),  # 所在地区
            'hot_orgs': hot_orgs,  # 热门机构
            'orgs': p.page(page)
        }

        return render(request, "org-list.html", ret)


class AddUserAskView(View):
    """
    “我要学习” 表单通过ajax提交的执行类。这里只返回json数据，不返回页面。
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)

        # 验证表单
        if userask_form.is_valid():
            userask_form.save(commit=True)  # 由于是ModelForm这里可以直接保存。
            ret = {
                'status': 'success',
                'msg': ''
            }
            return HttpResponse(json.dumps(ret), content_type='application/json')
        else:
            ret = {
                'status': 'fail',
                'msg': userask_form.errors
            }
            return HttpResponse(json.dumps(ret), content_type='application/json')


class OrgHome(View):
    """
    机构详情Home
    """
    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 取出被外键,Course中所对应course_org的数据(Course中course_org为本CourseOrg的数据)
        # 也就是-> 我被别人引用了，查出多少人引用了我，并返回引用我的人的信息
        all_courses = course_org.course_set.all()
        all_teachers = course_org.teacher_set.all() # 同上

        ret = {
            'course_org':course_org,
            'all_courses':all_courses,
            'all_teachers':all_teachers,
            "current_page":current_page, # 当前页标识，用于改变按钮样式
        }
        return render(request, "org-detail-homepage.html", ret)


class OrgCourse(View):
    """
    机构课程
    """
    def get(self, request, org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()

        ret = {
            'course_org': course_org,
            'all_courses': all_courses,
            "current_page": current_page, # 当前页标识，用于改变按钮样式
        }
        return render(request, "org-detail-course.html", ret)


class OrgDesc(View):
    """
    机构介绍
    """
    def get(self, request, org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))

        ret = {
            'course_org': course_org,
            "current_page": current_page, # 当前页标识，用于改变按钮样式
        }
        return render(request, "org-detail-desc.html", ret)


class OrgTeacher(View):
    """
    机构教师
    """
    def get(self, request, org_id):
        current_page = 'teachers'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teachers = course_org.teacher_set.all()  # 同上

        ret = {
            'course_org': course_org,
            'all_teachers': all_teachers,
            "current_page": current_page, # 当前页标识，用于改变按钮样式
        }
        return render(request, "org-detail-teachers.html", ret)

















