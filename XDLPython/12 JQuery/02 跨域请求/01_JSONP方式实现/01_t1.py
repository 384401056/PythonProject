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
       self.render('index.html')

    def post(self, *args, **kwargs):
        self.write('t1.post')


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
}

application = tornado.web.Application([
    (r'/index', IndexHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8081)
    tornado.ioloop.IOLoop.instance().start()
