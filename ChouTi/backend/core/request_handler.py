#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
from backend.session import session

class BaseRquestHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = session.SessionFactory.get_session_obj(self)

