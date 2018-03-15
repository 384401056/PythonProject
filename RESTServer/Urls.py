#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from Handlers import *

def make_app():
    return tornado.web.Application([
        (r"/fwk-service-parcel/parcel/queryParcel", QueryParcel),
        (r"/agrithings/mobile/agrithings/treasure/knowledge/content", KnowledgeContent),
    ])