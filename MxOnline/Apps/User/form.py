#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Blueice'
__date__ = '2018/6/14 13:27'

from django import forms

from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """
    表单验证类,这里的字段名要与form表单中input的name相对应
    """
    username = forms.CharField(required=True, min_length=5) # 不能为空,最小长度为5
    password = forms.CharField(required=True, min_length=8) # 不能为空,最小长度为8


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True) # 不能为空
    password = forms.CharField(required=True, min_length=8) # 不能为空,最小长度为8
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"}) # 验证码