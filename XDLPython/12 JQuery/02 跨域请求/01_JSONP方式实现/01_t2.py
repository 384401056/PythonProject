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


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 返回一个script函数式，t2.get就是要传递的数据。
        # 当Jsonp发起跨域请求后，就可以通过定义一个func名的函数，拿到其中参数，也就拿到了数据。
        # callbak请求参数就是客户端想要使用的函数名，根据函数名动态生成返回格式。
        callback = self.get_argument('callback')
        print(callback)
        self.write('%s(["t2.get","gaoyanbin","kkk"])' % callback)

    def post(self, *args, **kwargs):
        self.write('t2.post')


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
}

application = tornado.web.Application([
    (r'/index', IndexHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8082)
    tornado.ioloop.IOLoop.instance().start()
