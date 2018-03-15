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

class CorsHandler(tornado.web.RequestHandler):
    '''接收Ajax跨域请求的Handler'''

    def get(self, *args, **kwargs):
        self.write('Cors.get')

    def post(self, *args, **kwargs):
        # 设置返回数据的请求头，有此请求头后，浏览器就不会再阻止数据了。这样就允许客户端发送跨域请求(简单请求)了.
        # self.set_header('Access-Control-Allow-Origin', 'http://gyb.com:8081') # 指定域名，多域名可用逗号分隔。
        self.set_header('Access-Control-Allow-Origin', '*') # *号代表所有域名都可以

        self.write('Cors.post')

    def options(self, *args, **kwargs):
        '''接收预检请求'''

        # 告诉预检请求，允许当前域发来的请求。允许PUT请求。此时服务器端可以收到数据。只是客户端无法处理返回的数据
        # 预检请求通过后，就会收到put请求了。
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods','PUT') # 此参数可以为多个，但不能为*

        # 设置允许自定义请求头。
        self.set_header('Access-Control-Allow-Headers','k1')

        # 设置预检请求的过期时间.过期后要重发options.在过期时间以内只发put请求。
        self.set_header('Access-Control-Max-Age','10')

        '''
        可以options请里查看已经设置了的请求头信息：
        Access-Control-Allow-Headers:k1
        Access-Control-Allow-Methods:PUT
        Access-Control-Allow-Origin:*
        '''

        print('options')
        self.write('Cors.options')

    def put(self, *args, **kwargs):
        '''接收复杂请求'''

        print(self.get_argument('status'), self.get_argument('name'))
        # 告诉复杂请求，允许当前域发来的请求，这样客户端浏览器就可以接收从服务端返回的数据了。
        self.set_header('Access-Control-Allow-Origin', '*')
        self.write('Cors.put')


class CorsCookiesHander(tornado.web.RequestHandler):
    '''接收Ajax跨域请求,并携带cookies的请求。'''
    def get(self, *args, **kwargs):
        self.write('CorsCookies.get')

    def post(self, *args, **kwargs):
        self.write('CorsCookies.post')

    def options(self, *args, **kwargs):
        # 先允许域名，再允许put
        self.set_header('Access-Control-Allow-Origin', 'http://gyb.com:8081') # 要支持客户端携带cookies，此参数不能为*
        self.set_header('Access-Control-Allow-Methods', 'PUT')  # 此参数可以为多个，但不能为*

        # 允许自定义请求头。
        self.set_header('Access-Control-Allow-Headers', 'k1')

        # 允许携带cookies,put也要加上此设置
        self.set_header('Access-Control-Allow-Credentials', 'true')

        # 设置预检请求的过期时间.过期后要重发options.在过期时间以内只发put请求。
        self.set_header('Access-Control-Max-Age', '10')

        print('options')
        self.write('CorsCookies.options')

    def put(self, *args, **kwargs):
        self.set_cookie('t2_cookies', 'fdsafdsafdsafd')  # 设置cookies

        # 先允许域名, 再允许携带cookies
        self.set_header('Access-Control-Allow-Origin', 'http://gyb.com:8081') # 此语句要先允许，下面的设置请求头才生效
        self.set_header('Access-Control-Allow-Credentials', 'true')

        print('put')
        print(self.request.headers)
        print('%s , %s' % (self.get_argument('status'),self.get_argument('name')))

        self.write('CorsCookies.put')


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
}

application = tornado.web.Application([
    (r'/cors', CorsHandler),
    (r'/cookies', CorsCookiesHander),
], **settings)

if __name__ == '__main__':
    application.listen(8082)
    tornado.ioloop.IOLoop.instance().start()
