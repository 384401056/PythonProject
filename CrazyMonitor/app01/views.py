import json

from django.http import HttpResponse
from django.shortcuts import render
from CrazyMonitor import settings
from app01.backend import data_optimization
from app01.backend.redis_conn import redis_conn
from app01.serializer import ClientHandler

# Create your views here.

REDIS_OBJ = redis_conn(settings)  # 创建redis连接池.


def index(request):
    return render(request, 'app01/index.html')


def client_configs(request, client_id):
    """获取主机的监控服务配置信息"""
    # print('client_id:', client_id)
    config_obj = ClientHandler(client_id)
    config = config_obj.fech_configs()  # 获取监控服务配置信息

    if config:
        return HttpResponse(json.dumps(config))
    else:
        return HttpResponse(json.dumps(None))


def server_data_report(request):
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

            data_saving_obj = data_optimization.DataStore(client_id,server_name,json.loads(data), REDIS_OBJ)

            # 触发监控
            """
                ....
            """

        except IndexError as e:
            print('--->err:', e)

    return HttpResponse(json.dumps({'status': 'ok'}))
