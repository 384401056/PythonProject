#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import json
import tornado.httpserver
import tornado.options
import datetime

from tornado.web import RequestHandler
from tornado.options import define, options
from Handler import WebSocketHandler, SendHandler

app = tornado.web.Application([
    (r"/chat", WebSocketHandler),
    (r"/send", SendHandler),
])

if __name__ == '__main__':
    app.listen(address="0.0.0.0", port=5555)
    print("Tornado is running on http://127.0.0.1:5555")
    tornado.ioloop.IOLoop.instance().start()
