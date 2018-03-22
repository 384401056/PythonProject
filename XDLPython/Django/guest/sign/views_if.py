from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import *

# Create your views here.

ret = {
    'status': 0,
    'message': '',
    'data': {}
}


def add_event(request):
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
        except Exception as e:
            error = e.message
            ret['status'] = 10024
            ret['message'] = error
            return JsonResponse(ret)

        ret['status'] = 200
        ret['message'] = 'success'
        return JsonResponse(ret)

















