#!/usr/bin/env python
# -*- coding utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import time


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        if self.get_argument('u') in ['alex', 'gyb']:
            # self.set_cookie('name', self.get_argument('u')) # 设置普通cookies
            self.set_secure_cookie('name', self.get_argument('u'))  # 设置cookies加密签名
            self.write("设置cookies成功!!! ")
        else:
            self.write("请先登录.")


class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # if self.get_cookie('name') in ['alex', 'gyb']:

        cookie_name = str(self.get_secure_cookie('name'), encoding='utf-8')

        if cookie_name in ['alex', 'gyb']:
            # self.write("欢迎登录：" + self.get_cookie('name')) # 输出的是加密cookies的原始值.
            self.write("欢迎登录：" + cookie_name)
        else:
            self.write("请先登录.")


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
    'cookie_secret':'abcdefghijklmn', # 设置签名的key
}

application = tornado.web.Application([
    (r'/index', IndexHandler),
    (r'/manager', ManagerHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
