#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 20:46:34
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


import tornado.ioloop
import tornado.web
import os
import time

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        # self.set_cookie('key1', 'gaoyanbin1')
        # self.set_cookie('key2', 'gaoyanbin2')
        # self.set_cookie('key3', 'gaoyanbin3')
        # t = time.time()
        # expt = t + 5
        # print(self.set_cookie(name='key_tim', value='123321', expires=expt)) # 设置键值和超时时间expires(当前时间+多少)
        print(self.cookies) # 获取所有cookies
        print(self.get_cookie('key_tim')) # 获取单个cookie
        self.render('index.html')


        '''
        在浏览器的console中:
        document.cookie 查看浏览器的cookie
        document.cookie = 'kk=999' 设置cookie
        '''


application = tornado.web.Application([
    (r'/index', IndexHandler),
])

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
















