#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado
import json
from tornado.websocket import WebSocketHandler
from const import users, id
from model import User

class WebSocketHandler(tornado.websocket.WebSocketHandler):

    idx = 0
    user = {}

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求

    def open(self):
        users.add(self)  # 建立连接后添加用户到容器中
        idx+=id
        user = User(idx, self.request.remote_ip, self)
        users.add(user)
        # for u in users:
        #     u.write_message("Welcome to Tornado websocket!")
        print("%s is open." % self.request.remote_ip)

    def on_close(self):
        users.remove(user)  # 用户关闭连接后从容器中移除用户
        print("%s is close." % self.request.remote_ip)

    def on_message(self, message):
        # for u in users:
        #     u.write_message("form %s %s" % (self.request.remote_ip, message))
        print("%s is send %s" % (self.request.remote_ip, message))
        self.write_message("this is server message...")


class SendHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        for user in users:
            print(type(user))
            print(user.__dict__)
            user.handler.write_message("Ha Ha")
        self.write((json.dumps("OK")))
