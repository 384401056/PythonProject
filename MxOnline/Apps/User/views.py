# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import hashers
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from Apps.User.models import *
from Apps.User.form import *

from Apps.utils import send_email


# Create your views here.


class CustomBackend(ModelBackend):
    """
    自定义用户认证类, 当执行auth.authenticate()方法时，会转到这边来执行。
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 通过username获取数据库中的用户对象
            # 只要用户名匹配了username email 都是可以登录的
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))

            # 验证password是否正确。由于password在库中是密文存储，所以要用AbstractUser类提供的方法。
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ResetView(View):
    '''
    重置密码
    '''
    def get(self, request, code):
        record = EmailVerifyRecord.objects.filter(code=code).first()
        if record:
            user = UserProfile.objects.get(email=record.email)
            return render(request, "password_reset.html", {"email": user.email})
        else:
            return render(request, "active_fail.html")

class ModifyPwdView(View):
    def post(self, request):
        rest_form = ModifyPwdForm(request.POST)
        if rest_form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            password2 = request.POST.get("password")
            if password == password2:
                user = UserProfile.objects.get(email=email)
                user.password = hashers.make_password(password)  # 修改密码
                user.save()

                return render(request, "login.html")
            else:
                return render(request, "password_reset.html", {"msg": "两次输入密码不一致。"})

        else:
            return render(request, "password_reset.html", {"rest_form": rest_form})



class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            user = UserProfile.objects.filter(email=email).first()
            if user:
                # 发送忘记密码邮件
                send_email.send_register_email(user.email, type="forget")
                return render(request, "login.html")
            else:
                return render(request, "forgetpwd.html", {"msg": "用户不存在..."})
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ActiveUserVeiw(View):
    '''
    用户激活
    '''

    def get(self, request, code):
        record = EmailVerifyRecord.objects.filter(code=code).first()
        if record:
            user = UserProfile.objects.get(email=record.email)
            user.is_active = True
            user.save()
            return render(request, "login.html")
        else:
            return render(request, "active_fail.html")

    def post(self):
        pass


class RegisterView(View):
    """
    用户注册
    """

    def get(self, request):
        """
        用户注册
        :param request:
        :return:
        """
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            # 判断用户名是否已经存在.
            if UserProfile.objects.filter(email=email):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已经存在。"})
            else:
                # 创建新用户
                user = UserProfile()
                user.email = email
                user.username = email
                user.is_active = False
                user.password = hashers.make_password(password)  # 生成加密后的密码
                user.save()
                # 发送注册邮件
                send_email.send_register_email(user.email, type="register")
                return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


# 居于类的方式
class LoginView(View):
    """
    用户登陆View
    """

    def get(self, request):
        '''
        用户登录
        :param request:
        :return:
        '''
        return render(request, "login.html", {})

    def post(self, request):
        '''
        发送表单时获取数据
        :param request:
        :return:
        '''

        ret = {
            'data': None,
            'msg': None,
            'status': False
        }

        login_form = LoginForm(request.POST)

        # 如果form验证成功,则执行后面的逻辑。
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            '''
            使用Django的用户认证方法,默认的认证方法只能处理username的登录。
            使用自定义的认证方法，要在setting中加上 AUTHENTICATION_BACKENDS = () 指定认证的类
            并且此处代码不用更改
            '''
            user = auth.authenticate(username=user_name, password=pass_word)
            # 如果返回的user不为空则证明登陆成功
            if (user is not None) and (user.is_active):
                auth.login(request, user)
                ret['data'] = user # request中已经自带了一个user
                ret['status'] = True
                return render(request, "index.html", ret)
            # 否则就返回login页面。
            else:
                ret['msg'] = "用户不存在，或者账号未激活。"
                return render(request, "login.html", ret)
        else:
            return render(request, "login.html", {"login_form": login_form, "msg": "表单验证失败，请检查"})


# 居于方法的方式
def user_login(request):
    '''
    用户登录
    :param request:
    :return: 返回至首页
    '''
    ret = {
        'data': None,
        'msg': None,
        'status': False
    }

    # 点击链接时进行登录页面
    if request.method == "GET":
        return render(request, "login.html", {})
    # 发送表单时获取数据
    elif request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")

        '''
        使用Django的用户认证方法,默认的认证方法只能处理username的登录。
        使用自定义的认证方法，要在setting中加上 AUTHENTICATION_BACKENDS = () 指定认证的类
        并且此处代码不用更改
        '''
        user = auth.authenticate(username=user_name, password=pass_word)
        if user is not None:
            auth.login(request, user)
            ret['data'] = user
            ret['status'] = True
            return render(request, "index.html", ret)
        else:
            ret['msg'] = "用户名密码错误"
            return render(request, "login.html", ret)
