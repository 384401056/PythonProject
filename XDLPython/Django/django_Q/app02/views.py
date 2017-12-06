from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from . import models
from django.db.models import F, Q, Count
import json
from .forms import LoginForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        return index_post(request)
    else:
        return index_get(request)


def index_post(request):
    result = {'status': True, 'msg': '', 'data': None}
    try:
        post_data = request.POST.get('post_data', None)
        if post_data is not None:
            post_data_dict = json.loads(post_data)
            con = Q()
            for k, v in post_data_dict.items():
                q1 = Q()
                q1.connector = 'OR'
                for item in v:
                    q1.children.append((k, item))
                con.add(q1, 'AND')

            ret = models.Book.objects.filter(con).values('name', 'page', 'price', 'pubdate', 'book_type__caption')
            print(ret)
            ret_list = list(ret)
            result['status'] = True
            result['data'] = ret_list
    except Exception as e:
        result['msg'] = str(e)

    # 使用自定义解析器,解析Django中的DateTimeField和DecimalField
    from .tests import JsonCustomEncoder
    return HttpResponse(json.dumps(result, cls=JsonCustomEncoder))


def index_get(request):
    return HttpResponse('Get OK')


def login(request):
    if request.method == 'POST':
        return login_post(request)
    else:
        return login_get(request)


def login_post(request):
    result = {'status': True, 'msg': '', 'data': None}

    # request.POST.get('username', None)
    # request.POST.get('pwd', None)

    # 创建Form对象
    f = LoginForm(request.POST)

    if f.is_valid():
        result['status'] = True
    else:
        result['status'] = False
        result['msg'] = f.errors

        # 直接打印输出，为html格式。
        # print(f.errors)
        # print(f.errors['username'][0])
        # print(f.errors['pwd'][0])

    result['data'] = f.cleaned_data

    # 使用自定义解析器,解析Django中的DateTimeField和DecimalField
    # from .tests import JsonCustomEncoder
    # return_json = json.dumps(result, cls=JsonCustomEncoder)
    # return HttpResponse(json.dumps(result, cls=JsonCustomEncoder))
    # return render(request, 'login.html', {'return_json':result})
    return render(request, 'login.html', {'error':f.errors})

def login_get(request):
    pass
















