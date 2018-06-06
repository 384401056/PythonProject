#!/usr/bin/env python
# -*- coding: utf-8 -*-

class User(object):

    def __init__(self, id, ip, handler):
        self.id = id
        self.ip = ip
        self.handler = handler