from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import *
from django.forms.models import model_to_dict
from django.core import serializers
import json

# Create your views here.




def add_event(request):
    """添加发布会接口"""
    ret = {
        'status': 0,
        'message': '',
        'data': {}
    }
    if request.method == 'POST':
        # eid = request.POST.get('eid', '')
        name = request.POST.get('name', '')
        limit = request.POST.get('limit', '')
        status = request.POST.get('status')
        address = request.POST.get('address', '')
        start_time = request.POST.get('start_time', '')

        if name == '' or limit == '' or address == '' or start_time == '':
            ret['status'] = 10021
            ret['message'] = '参数错误!'
            return JsonResponse(ret)

        if Event.objects.filter(name == name) is not None:
            ret['status'] = 10023
            ret['message'] = '发布会名已存在!'
            return JsonResponse(ret)

        if status == '':
            status = 1

        try:
            Event.objects.create(name=name, limit=limit, status=int(status), address=address,
                                 start_time=start_time)
            ret['status'] = 200
            ret['message'] = 'success'
        except Exception as e:
            error = str(e)
            ret['status'] = 10024
            ret['message'] = error
        finally:
            return JsonResponse(ret)


def get_event_info(request):
    """通过edi和name参数获取发布会信息"""
    ret = {
        'status': 0,
        'message': '',
        'data': {}
    }

    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')

    # if name == '' or eid == '':
    #     ret['status'] = 10021
    #     ret['message'] = '参数错误!'
    #     return JsonResponse(ret)

    if eid != '':
        try:
            result = Event.objects.get(id=eid)
            ret['status'] = 200
            ret['message'] = 'success'
            # 将object.get()得到的对象，转为字典数据。
            ret['data'] = model_to_dict(result)
        except Exception as e:
            ret['status'] = 10022
            ret['message'] = str(e)
        finally:
            return JsonResponse(ret)

    if name != '':
        try:
            # result = Event.objects.filter(name=name).first() # 只取第一个返回 Event对象
            result = Event.objects.filter(name=name).values() # 取所有，返回 QuerySet
            # print(type(result))
            ret['status'] = 200
            ret['message'] = 'success'
            # ret['data'] = model_to_dict(result) # 当result是model对象时，使用此方法来转为json
            ret['data'] = list(result) # 当result为QuerySet类型时，使用此方法来转json
        except Exception as e:
            ret['status'] = 10022
            ret['message'] = str(e)
        finally:
            return JsonResponse(ret)


def add_guest(request):
    if request.method == 'POST':
        realname = request.POST.get('realname','')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

