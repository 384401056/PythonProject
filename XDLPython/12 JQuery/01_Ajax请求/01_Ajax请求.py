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



IMG_LIST = []


class BaseHandle(tornado.web.RequestHandler):
    '''
    创建一个公共的父类，初始化时创建session.(RequestHandler原码中的initialize方法是在__init__方法最后执行的。)
    这样的话，在IndexHandler，ManagerHandler中就不用创建Session对象了。
    '''
    def initialize(self):
        pass


class IndexHandler(BaseHandle):
    def get(self, *args, **kwargs):
        self.render('index.html')

class GetDataHandler(BaseHandle):
    def get(self, *args, **kwargs):
        print(self.get_argument('name'))
        self.write('Hello Ajax!')

    def post(self, *args, **kwargs):
        print(self.get_argument('name'))
        self.write('Hello Ajax Post')


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
}

application = tornado.web.Application([
    (r'/index', IndexHandler),
    (r'/getdata', GetDataHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
