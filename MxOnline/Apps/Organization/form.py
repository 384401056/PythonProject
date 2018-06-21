#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Blueice'
__date__ = '2018/6/19 15:40'

from django import forms
from Apps.Operation.models import *
import re


# 使用ModelForm, 通过model来生成需要提交的form
class UserAskForm(forms.ModelForm):
    # 新增自定义字段
    # new_field = forms.CharField(max_length=2)
    class Meta:
        # 继承自UserAsk model
        model = UserAsk

        # 指定要使用的字段，此字段要与form表单中的input name相对应
        fields = [
            'name',
            'mobile',
            'course_name',
        ]

    def clean_mobile(self):
        """
        自定义的验证方法
        :return:
        """
        mobile = self.cleaned_data['mobile'] # 取出mobile的值
        regex_mobile = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$"
        p = re.compile(regex_mobile)

        # 如果手机号匹配，则返回手机号，否则抛出异常,些异常在forms.errors中可捕获。
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码不正确。")
