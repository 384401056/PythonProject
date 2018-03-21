from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')


def login_action(request):
    """用户登陆"""
    if request.method == 'POST':
        username = request.POST.get('username','')
        pwd = request.POST.get('password','')
        user = auth.authenticate(username=username, password=pwd)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username # 添加浏览器session.
            # response.set_cookie('user', username, 3600) # 添加浏览器cookie,3600秒为cookie保存时间。

            response = HttpResponseRedirect('/even_manage/')
            return response

        else:
            return render(request, 'index.html',{'error':'用户名密码错误'})


@login_required
def even_manage(request):
    # username = request.COOKIES.get('user','') # 读取浏览器cookie
    event_list = Event.objects.all()
    username = request.session.get('user','') # 读取浏览器session
    return render(request, 'event_manage.html', {'user':username,'event_list':event_list})

@login_required
def gues_manage(request):
    pass


@login_required
def search_name(request):
    if request.method == 'GET':
        username = request.session.get('user', '')
        keyword = request.GET.get('keyword', '')
        event_list = Event.objects.filter(name__contains=keyword)
        return render(request, 'event_manage.html', {'user': username, 'event_list': event_list})

