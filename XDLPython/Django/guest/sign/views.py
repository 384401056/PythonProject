from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from sign.models import *

# Create your views here.

PAGE_SIZE = 10

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
            response = HttpResponseRedirect(reverse('event_manage'))
            return response
        else:
            return render(request, 'index.html',{'error':'用户名密码错误'})

@login_required
def event_manage(request):
    """发布会管理"""
    if request.method == 'GET':
        pageNumber = request.GET.get('pageNumber', '1')  # 默认为第一页
        # username = request.COOKIES.get('user','') # 读取浏览器cookie
        username = request.session.get('user','') # 读取浏览器session
        event_list = Event.objects.all().order_by('id')# 为了保证分页序号一至，所以要进行排序。默认objects.all()返回的是无序列表
        paginator = Paginator(event_list, PAGE_SIZE)  # 3是page_size，每页多少条

        try:
            contacts = paginator.page(pageNumber)
        except PageNotAnInteger: # 如果pageNumber不是整数，跳至page(1)
            contacts = paginator.page(1)
        except EmptyPage:  # 如果没有这页，跳至最后一页。
            contacts = paginator.page(paginator.num_pages)

        return render(request, 'event_manage.html', {'user':username,'event_list':contacts})

@login_required
def guest_manage(request):
    """嘉宾管理"""
    if request.method=='GET':
        pageNumber = request.GET.get('pageNumber','1') # 默认为第一页
        username = request.session.get('user', '')  # 读取浏览器session
        guest_list = Guest.objects.all().order_by('id') # 为了保证分页序号一至，所以要进行排序。默认objects.all()返回的是无序列表
        paginator = Paginator(guest_list, PAGE_SIZE) # 3是page_size，每页多少条
        try:
            contacts = paginator.page(pageNumber)
        except PageNotAnInteger: # 如果pageNumber不是整数，跳至page(1)
            contacts = paginator.page(1)
        except EmptyPage:  # 如果没有这页，跳至最后一页。
            contacts = paginator.page(paginator.num_pages)

        return render(request, 'guest_manage.html', {'user': username, 'guest_list': contacts})


@login_required
def search_even(request):
    """发布会搜索"""
    if request.method == 'GET':
        pageNumber = request.GET.get('pageNumber', '1')
        username = request.session.get('user', '')
        keyword = request.GET.get('keyword', '')
        event_list = Event.objects.filter(name__contains=keyword).order_by('id')
        paginator = Paginator(event_list, PAGE_SIZE)  # 3是page_size，每页多少条

        try:
            contacts = paginator.page(pageNumber)
        except PageNotAnInteger: # 如果pageNumber不是整数，跳至page(1)
            contacts = paginator.page(1)
        except EmptyPage:  # 如果没有这页，跳至最后一页。
            contacts = paginator.page(paginator.num_pages)
        return render(request, 'event_manage.html', {'user': username, 'event_list': contacts, 'keyword':keyword})


@login_required
def search_gues(request):
    """嘉宾搜索"""
    if request.method == 'GET':
        pageNumber = request.GET.get('pageNumber', '1')
        username = request.session.get('user', '')
        keyword = request.GET.get('keyword', '')
        guest_list = Guest.objects.filter(realname__contains=keyword).order_by('id')
        paginator = Paginator(guest_list, PAGE_SIZE)  # 3是page_size，每页多少条

        try:
            contacts = paginator.page(pageNumber)
        except PageNotAnInteger: # 如果pageNumber不是整数，跳至page(1)
            contacts = paginator.page(1)
        except EmptyPage:  # 如果没有这页，跳至最后一页。
            contacts = paginator.page(paginator.num_pages)

        return render(request, 'guest_manage.html', {'user': username, 'guest_list': contacts, 'keyword':keyword})

@login_required
def logout(request):
    if request.method == 'GET':
        auth.logout(request) # 退出登录
        return HttpResponseRedirect(reverse('index'))


















