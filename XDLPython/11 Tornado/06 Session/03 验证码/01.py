#!/usr/bin/env python
# -*- coding utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import time
import hashlib
import io
from VerifyCode import *

# 存储session信息的字典.一般放在radis中。
container = dict()


class Session:
    def __init__(self, handler):
        self.handler = handler
        self.md5_str = None

    '''将原来的set_value方法写在 __setitem__中后，就可以 seesion['key'] = value 这样来使用session对象了.'''

    def __setitem__(self, key, value):
        self.set_value(key, value)

    '''将原来的get_value方法写在 __getitem__中后，就可以 seesion['key'] 这样来使用session对象了.'''

    def __getitem__(self, item):
        return self.get_value(item)

    '''生成MD5码'''

    def __get_md5_str(self):
        obj = hashlib.md5()
        md5_bytes = bytes(str(time.time()), encoding='utf-8')
        obj.update(md5_bytes)
        md5_str = obj.hexdigest()
        return md5_str

    def set_value(self, key, value):
        if not self.md5_str:
            md5_str = self.handler.get_cookie('user_identity', None)
            # 如果客户端没有随机MD5码
            if not md5_str:
                # 生成md5码
                md5_str = self.__get_md5_str()
                # 则创建新的md5码和用户信息空字典。
                container[md5_str] = {}
            else:
                # 如果客户端有md5,但服务器端由于重启了，没有md5了.则创建新的md5码和用户信息空字典。
                if not (md5_str in container.keys()):
                    # 生成md5码
                    md5_str = self.__get_md5_str()
                    container[md5_str] = {}
                else:
                    # 如果两边都有md5,则什么也不用做。
                    pass
            self.md5_str = md5_str
        # 设置用户信息
        container[self.md5_str][key] = value
        # 将生成的MD5k唯一标识写入客户端的cookeis中
        # 此处写入是为了以后更新失效时间。
        self.handler.set_cookie('user_identity', self.md5_str)

    def get_value(self, key):
        md5_str = self.handler.get_cookie('user_identity', None)

        # 如果没有md5,则返回None
        if not md5_str:
            return None

        user_info = container.get(md5_str, None)  # 通过md5码获取container中的用户信息。
        # 如果服务器端没有user_info
        if not user_info:
            return None
        return user_info.get(key, None)


class BaseHandle(tornado.web.RequestHandler):
    '''
    创建一个公共的父类，初始化时创建session.(RequestHandler原码中的initialize方法是在__init__方法最后执行的。)
    这样的话，在IndexHandler，ManagerHandler中就不用创建Session对象了。
    '''

    def initialize(self):
        self.session = Session(self)


class IndexHandler(BaseHandle):
    def get(self, *args, **kwargs):
        # 如果用户名正确
        if self.get_argument('u', None) in ['alex', 'gyb']:

            # 用字典的方法来设置seesion中的值
            self.session['is_login'] = True
            self.session['name'] = self.get_argument('u')
            self.write(container)
        else:
            self.write('用户名错误！')


class ManagerHandler(BaseHandle):
    def get(self, *args, **kwargs):

        # 用字典的方法来获取seesion中的值
        if self.session['is_login']:
            is_login = str(self.session['is_login'])
            name = str(self.session['name'])
            self.write(bytes('is_login: %s,  name: %s' % (is_login, name), encoding='utf-8'))
        else:
            self.write('还没登录.')


class LoginHandler(BaseHandle):
    def get(self, *args, **kwargs):
        self.render('login.html', status='')

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        pwd = self.get_argument('pwd')
        code = self.get_argument('code')
        check_code = self.session['code']
        # 如果参数中的验证码与seesion中的验证码一致。
        if code.upper() == check_code.upper():
            self.write('验证码正确!')
        else:
            self.render('login.html', status='验证码错误')


class CheckCodeHandler(BaseHandle):
    '''生成验证码图片，并设置cookies中的session'''

    def get(self, *args, **kwargs):
        '''生成验证码图片，并返回'''
        vecode = VerifyCode()
        code_img, capacha_code = vecode.createCodeImage()
        msstream = io.BytesIO()
        code_img.save(msstream, "jpeg")
        code_img.close()
        self.session['code'] = capacha_code  # 将capacha_code保存进seesion中。
        self.set_header('Content-Type', 'image/jpg')  # 设置头类型
        self.write(msstream.getvalue())  # 返回IO流中的数据。


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
    'cookie_secret': 'gaoyanbin',  # 设置签名的key
}

application = tornado.web.Application([
    (r'/index', IndexHandler),
    (r'/manager', ManagerHandler),
    (r'/login', LoginHandler),
    (r'/check_code', CheckCodeHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
