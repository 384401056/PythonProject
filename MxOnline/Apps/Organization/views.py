from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from Apps.Organization.models import *
from MxOnline import settings

# Create your views here.



class OrgListView(View):
    '''
    课程机构列表
    '''

    def get(self, request):
        ret = {}
        orgs = CourseOrg.objects.all()  # 机构列表
        ret['cities'] = CityDict.objects.all()  # 所在地区
        ret['org_num'] = orgs.count()  # 机构数量
        try:
            page = request.GET.get("page", 1)  # 获取页码，默认为1
        except PageNotAnInteger:
            page = 1

        # 创建分页对象。
        p = Paginator(orgs, request=request, per_page=4) # per_page每页数
        # per_page = settings.PAGINATION_SETTINGS['PAGE_RANGE_DISPLAYED'] # 每页数

        ret['orgs'] = p.page(page)  # 获取分页后的数据

        return render(request, "org-list.html", ret)
