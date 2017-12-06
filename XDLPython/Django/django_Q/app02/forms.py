#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import forms

"""登录表单的验证类"""
class LoginForm(forms.Form):
    username = forms.CharField()
    pwd = forms.CharField()
