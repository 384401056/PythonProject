#!/usr/bin/env python
# -*- coding utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import time
import hashlib
import io
from PIL import Image
import os
import re

'''当有多个表单的验证类时，可以将类的公共部分提取出，封装为Form表单验证的基类'''
class BaseForm:

    def check_valid(self, handler):
        """
        检查表单提交的内容，是否符合要求。
        :param handler:
        :return:
        """
        flag = True
        value_dict = {}
        for key, value_zz in self.__dict__.items():  # __dict__.items() 就是IndexForm类的成员变量键值对列表。
            input_value = handler.get_argument(key)
            value_dict[key] = input_value
            # 　循环取出用户的值，与正则进行匹配。如果不成功则值为None
            val = re.match(value_zz, input_value)
            if not val: # 只要有一个匹配不成功，就返回false
                flag = False
        return flag, value_dict

'''进行Index页面Form表单验证的类'''
class IndexForm(BaseForm):
    def __init__(self):
        # Form表单中，需要进行验证的正则表达式。
        self.host = "(.*)"  # 主机名
        self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"# 匹配ip地址
        self.port = '(\d+)'  # 端口号
        self.phone = '^1[3|4|5|8][0-9]\d{8}$'  # 手机号

    # def check_valid(self, handler):
    #     flag = True
    #     value_dict = {}
    #     for key, value_zz in self.__dict__.items():  # __dict__.items() 就是IndexForm类的成员变量键值对列表。
    #         input_value = handler.get_argument(key)
    #         value_dict[key] = input_value
    #         # 　循环取出用户的值，与正则进行匹配。如果不成功则值为None
    #         val = re.match(value_zz, input_value)
    #         if not val: # 只要有一个匹配不成功，就返回false
    #             flag = False
    #     return flag, value_dict

'''进行User页面Form表单验证的类'''
class UserForm(BaseForm):
    def __init__(self):
        # Form表单中，需要进行验证的正则表达式。
        self.host = "(.*)"  # 主机名
        self.aa = IPField
        self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"# 匹配ip地址


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self, *args, **kwargs):
        obj = IndexForm()
        flag, value_dict = obj.check_valid(self)
        print(flag, value_dict)
        self.write('post')


class UserHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('user.html')

    def post(self, *args, **kwargs):
        obj = UserForm()
        flag, value_dict = obj.check_valid(self)
        print(flag, value_dict)
        self.write('post')


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
}

application = tornado.web.Application([
    (r'/index', IndexHandler),
    (r'/user', UserHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
