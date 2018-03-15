#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import os


class MainHandler(tornado.web.RequestHandler):



    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self, *args, **kwargs):
        # self.write("Hello 11 Tornado!") # 返回数据
        self.render(os.path.join('html', 'user.html'))  # 返回网页模板

    def post(self, *args, **kwargs):
        print(self.get_body_argument(name='a2'))  # 获取参数
        print(self.get_argument(name='a1'))
        print(self.redirect())
        self.write("hello tornado!")


application = tornado.web.Application([
    (r'/index', MainHandler),
])

if __name__ == '__main__':
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
