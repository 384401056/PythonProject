"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from sign import views
#利用TemplateView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^login_action/$', views.login_action, name='login_action'),
    url(r'^event_manage/$', views.event_manage, name='event_manage'),
    url(r'^guest_manage/$', views.guest_manage, name='guest_manage'),
    url(r'^search_even/$', views.search_even, name='search_even'),
    url(r'^search_gues/$', views.search_gues, name='search_gues'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^accounts/login/$', views.index),# 用户没有登录时的url路由

    # API接口
    url(r'^api/', include('sign.urls_api')),


]
