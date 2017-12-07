#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from django import forms
from django.core.exceptions import ValidationError

from . import models

# 自定义格式校验方法。用为验证手机号是否正确的。
def MobileValidators(value):
    mobile_re = re.compile(r'^1[34578]\d{9}$',)

    if not mobile_re.match(value):
        raise ValidationError('手机号码不正确。')




"""登录表单的验证类"""
class LoginForm(forms.Form):
    # required 是否可以为空,max_length,min_length最大最小长度
    username = forms.CharField(
        # required=False,# required 是否可以为空
        # max_length=10,# max_length,min_length最大最小长度
        # min_length=2,
        # error_messages={'required': '不为空提示信息', 'invalid': '格式错误'},# error_message 错误提交信息
        # widget=forms.TextInput(attrs={'class':'content-text'}), # 指定html控件,并指定class样式
        # validators=[] # 自定义格式校验方法
    )

    pwd = forms.CharField()


    memo= forms.CharField(
        widget=forms.Textarea()
    )


    phone = forms.CharField(
        validators=[MobileValidators,],
        error_messages = {'required': '不为空提示信息'},
    )


    # choice=(
    #     (0, '普通用户'),
    #     (1, '高级用户'),
    # )

    # 从数据库取列表项,但是由于，username，pwd，booktype..都是LoginForm中的静态字段，
    # 所以当数据库中的值改变时，页面并不会动态更新.为了实现动态更新要重写自定义的__init__()方法中
    choice = models.BookType.objects.all().values_list('id','caption')
    print(choice)
    booktype = forms.CharField(
        widget=forms.widgets.Select(choices=choice)
    )

    # booktype 放在__init__方法中，每次刷新都会重新加载数据库数据。
    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)

        choice = models.BookType.objects.all().values_list('id', 'caption')

        self.fields['booktype']= forms.CharField(
            widget=forms.widgets.Select(choices=choice)
        )