#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web

class BaseRquestHandler(tornado.web.RequestHandler):
    def initialize(self):
        # self.session = SessionFactory.get_session_obj(self)
        pass
