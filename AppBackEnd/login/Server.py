#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop

from Urls import *

if __name__ == "__main__":
    app = make_app()
    app.listen(address="0.0.0.0",port=5764)
    print("Server start on 5764!")
    tornado.ioloop.IOLoop.current().start()