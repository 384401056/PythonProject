#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

class MongoDBConn:

    def __init__(self, path="localhost", port=27017 ,db_name='mytest', set_name='test'):
        self.client = MongoClient(path, port)
        self.db = self.client[db_name]
        self.set_name = set_name

    def getSet(self):
        return self.db[self.set_name]