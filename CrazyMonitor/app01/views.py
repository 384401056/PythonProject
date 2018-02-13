#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from CrazyMonitor import settings
from app01.backend import data_optimization
from app01.backend.redis_conn import redis_conn
from app01.serializer import ClientHandler, get_host_trgger
from app01 import models
from app01.backend import data_processing, data_collection
from django.core.serializers import serialize

# Create your views here.

REDIS_OBJ = redis_conn(settings)  # 创建redis连接池.
collection = data_collection.Collection(redis_conn=REDIS_OBJ)


def get_all_hostgroup(request):
    '''
    获取所有主机组列表
    :param request:
    :return:
    '''
    ret = collection.get_all_hostgroup()
    return JsonResponse(ret)


def get_hosts_by_groupid(request, group_id):
    '''
    根据主机组id获取主机列表
    :param request:
    :return:
    '''
    ret = collection.get_hosts_by_groupid(group_id)
    return JsonResponse(ret)

def get_real_data_by_hostid(request, host_id):
    '''
    根据主机id和flag来获取主机的最新数据
    :param request:
    :param host_id:
    :param flag:
    :return:
    '''
    ret = collection.get_redis_data_by_hostid(host_id, -1)
    return JsonResponse(ret, safe=False)


def get_all_data_by_hostid(request, host_id):
    '''
    根据主机id和flag来获取主机所有数据
    :param request:
    :param host_id:
    :return:
    '''
    ret = collection.get_redis_data_by_hostid(host_id, 0)
    return JsonResponse(ret, safe=False)







def client_configs(request, client_id):
    '''
    让客户端程序从服务器获取主机的监控服务配置信息
    :param request:
    :param client_id: 客户端id
    :return:
    '''
    # print('client_id:', client_id)
    config_obj = ClientHandler(client_id)
    config = config_obj.fech_configs()  # 获取监控服务配置信息

    if config:
        return HttpResponse(json.dumps(config))
    else:
        return HttpResponse(json.dumps(None))

def server_data_report(request):
    """
    保存上报数据
    :param request:
    :return:
    """
    if request.method == 'POST':
        try:
            client_id = request.POST.get('client_id', None)
            server_name = request.POST.get('server_name', None)
            data = request.POST.get('data', None)
            post_data = {
                'client_id:': client_id,
                'server_name:': server_name,
                'data:': data,
            }
            print(post_data)

            # 处理并保存数据
            data_saving_obj = data_optimization.DataStore(client_id, server_name, json.loads(data), REDIS_OBJ)

            """
            触发监控
            """
            host_obj = models.Host.objects.get(id=int(client_id))
            server_triggers = get_host_trgger(host_obj)
            trigger_handler = data_processing.DataHandler(settings, connect_redis=False)

            # 循环多种Service类的trigger，同类的trigger可以一起处理。
            for trigger in server_triggers:
                trigger_handler.load_service_data_and_calulating(host_obj, trigger, REDIS_OBJ)

            print('server_triggers:', server_triggers)

        except IndexError as e:
            print('--->err:', e)

    return HttpResponse(json.dumps({'status': 'ok'}))

def test(request):
    ret = collection.get_redis_data_by_hostid(1,-1)
    return JsonResponse(ret,safe=False)
    pass
    # # 从redis中取出的原始数据，从最后一个（-1)开始，往前取 approximate_data_points 个
    # data_range_raw = REDIS_OBJ.lrange('StatusData_1_LinuxNIC_latest', -10, -1)
    #
    # # 获得大概的数据列表。
    # approximate_data_range = [json.loads(item) for item in data_range_raw]  # 列表推导式,返回的数据要进行返序列化处理。
    #
    # data_range = []  # 用于保存精确数据
    #
    # for data, time in approximate_data_range:
    #     print(json.dumps(data), time)


    # host_obj = models.Host.objects.get(id=1)
    # triggers = []
    # for tem in host_obj.templates.select_related():
    #     triggers.extend(tem.trigger.select_related())
    #
    # groups_obj = host_obj.host_group.select_related()
    # for group in groups_obj:
    #     for tem in group.templates.select_related():
    #         triggers.extend(tem.trigger.select_related())
    #
    # print('Triggers:', triggers)
    #
    #
    # for trigger in set(triggers):
    #     for expression in trigger.triggerexpression_set.select_related().order_by('id'):
    #         print('Expression:',expression)


    # obj = models.Trigger.objects.get(id=2)
    #
    # print(type(obj))



    # te_list = list(models.TriggerExpression.objects.all().values('trigger','service','threshold'))
    # print(te_list)


    # host_list = models.Host.objects.filter(status=1)
    #
    # for host in host_list:
    #     print(host)
    #
    # return HttpResponse('Test View!')
