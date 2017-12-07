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
    # post���ݸ�ʽ {"post_data":{"name":["��������", "Springʵս"], "price":["3209.5"]}}
    # �ֵ�Ԫ��post_data����AND�Ĺ�ϵ���ֵ���ֵ��ڲ���OR�Ĺ�ϵ
    post_data = request.POST.get('post_data', None)
    if post_data is not None:
        post_data_dict = json.loads(post_data) # �������������ַ�תΪ����
        print(post_data_dict)
        con = Q()
        for k, v  in post_data_dict.items():
            q1 = Q()
            q1.connector = 'OR'

            for item in v:
                q1.children.append((k,item))

            # ѭ����Ӳ�ѯ����
            con.add(q1, 'AND')

        # Django�����json���򶨴���
        # ret = models.Book.objects.filter(con)
        # json_ret = serializers.serialize('json', ret)
        # print(type(json_ret), json_ret)

        ret = models.Book.objects.filter(con).values('name','page','book_type__caption')
        li = list(ret) # ���ret���б�ṹ������,���������ּ򵥵ķ�ʽ��תΪpython���б����͡�
        print(type(li), li)
        # python���б����;Ϳ�����json.dumps()������ת���ˡ�
        # ����Django��Decimal��Date���͵��ֶ���ʹ��json.dumps()ʱ,��Ҫ����һЩ����Ĳ�����
        result = json.dumps(li)

    return HttpResponse(result)

def index_get(request):

    return HttpResponse('OK')



