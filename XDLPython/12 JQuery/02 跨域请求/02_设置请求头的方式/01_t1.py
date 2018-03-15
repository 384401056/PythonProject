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

'''
设置请求头的本质：客户端不变，服务器端设置请求头。其中又分为：
1. 简单请求。
2. 复杂请求。复杂请求会先发一个options请求，对服务器进行预访问。然后才发送正真的PUT，DELETE请求等
'''


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('cors.html')

    def post(self, *args, **kwargs):
        self.write('t1.post')


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
}

application = tornado.web.Application([
    (r'/cors', IndexHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8081)
    tornado.ioloop.IOLoop.instance().start()
