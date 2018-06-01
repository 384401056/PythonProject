#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import json


class MainHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self, *args, **kwargs):
        # 获取参数
        print('arguments: ', self.request.arguments)
        # print('argument:', self.get_argument(name='a1', default=None))
        # print('argument:', self.get_argument(name='a2', default=None))
        self.write((json.dumps("Get Hello Tornado!")))

    def post(self, *args, **kwargs):
        print('arguments: ', self.request.arguments)
        # print('argument:', self.get_argument('name', ''))
        # print('argument:', self.get_argument('age', 0))
        # print('argument:', self.get_argument('sex', ''))
        self.write((json.dumps("Post Hello Tornado!")))


application = tornado.web.Application([
    (r'/index', MainHandler),
])

if __name__ == '__main__':
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()