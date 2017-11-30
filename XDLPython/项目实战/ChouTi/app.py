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
from controllers import home, account

settings = {
    'template_path': 'views',
    'static_path': 'statics',  # 静态资源的路径
    'static_url_prefix': '/statics/',  # 静态资源的前缀
}

application = tornado.web.Application([
    (r'/index', home.IndexHandler),
    (r'/send_code', account.SendCodeHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
