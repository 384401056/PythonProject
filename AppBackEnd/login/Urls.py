#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from Handlers import *

def make_app():
    return tornado.web.Application([
        (r"/login", Login),
        (r"/user/info", UserInfo),
    ])