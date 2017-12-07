from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from . import models
from django.db.models import F,Q,Count
from django.core import serializers
import json


# Create your views here.

def  index(request):

    if request.method=='POST':
        return index_post(request)
    else:
        return index_get(request)


def index_post(request):
    # post数据格式 {"post_data":{"name":["葵花宝典", "Spring实战"], "price":["3209.5"]}}
    # 字典元素post_data内是AND的关系，字典的字典内部是OR的关系
    post_data = request.POST.get('post_data', None)
    if post_data is not None:
        post_data_dict = json.loads(post_data) # 将参数传来的字符转为对象
        print(post_data_dict)
        con = Q()
        for k, v  in post_data_dict.items():
            q1 = Q()
            q1.connector = 'OR'

            for item in v:
                q1.children.append((k,item))

            # 循环添加查询条件
            con.add(q1, 'AND')

        # Django输入出json的因定搭配
        # ret = models.Book.objects.filter(con)
        # json_ret = serializers.serialize('json', ret)
        # print(type(json_ret), json_ret)

        ret = models.Book.objects.filter(con).values('name','page','book_type__caption')
        li = list(ret) # 如果ret是列表结构的数据,可以用这种简单的方式来转为python的列表类型。
        print(type(li), li)
        # python的列表类型就可以用json.dumps()来进行转换了。
        # 但是Django中Decimal和Date类型的字段在使用json.dumps()时,需要进行一些特殊的操作。
        result = json.dumps(li)

    return HttpResponse(result)

def index_get(request):

    return HttpResponse('OK')



