"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
import xadmin
from Apps.User.views import *
import Apps.Organization
from Apps.Organization.views import *
from django.views.static import serve # 处理静态资源的服务
import captcha
from MxOnline.settings import MEDIA_ROOT

urlpatterns = [
    path(r'xadmin/', xadmin.site.urls),
    path(r'', TemplateView.as_view(template_name="index.html"), name="index"),
    # path(r'login/', TemplateView.as_view(template_name="login.html"), name="login"), # 跳转到静态html页面
    # path(r'login/', user_login, name="login")
    path(r'login/', LoginView.as_view(), name="login"),  # 使用类来处理路由, 处理用户登录请求
    path(r'register/', RegisterView.as_view(), name="register"),  # 处理用户注册请求
    path(r'active/<str:code>', ActiveUserVeiw.as_view(), name="activeUser"),
    path(r'captcha/', include('captcha.urls')), # 处理注册验证码的路由
    path(r'forget/', ForgetPwdView.as_view(), name="forget_pwd"),
    path(r'reset/<str:code>', ResetView.as_view(), name="reset_pwd"),
    path(r'modifypwd/', ModifyPwdView.as_view(), name="modify_pwd"),

    re_path(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}), # 静态图片的url处理。

    # path(r'orglist/', OrgListView.as_view(), name="org_list"),

    # 在Django2.0中，使用app_name的形式将namespace定义到 include 的 urls 文件中。
    path(r'org/', include('Organization.urls')),


]
