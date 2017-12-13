#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print self.request
        self.write("Hello Tornado!") # 返回数据
        # self.render(os.path.join('html', 'user.html'))  # 返回网页模板

    def post(self, *args, **kwargs):
        # print self.request
        print self.get_body_argument(name='payload')
        self.write("hello tornado!")


application = tornado.web.Application([
    (r'/coap', MainHandler),
])

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
