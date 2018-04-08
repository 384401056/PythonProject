#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import json
from time import time
from datetime import datetime


def insertInt():
    client = MongoClient('192.168.1.102', 27017)
    db = client['mytest']
    collection = db['number']

    # 插入整数, python3.x 去除了long
    collection.insert({
        "num": 200,
    })

    collection.insert({
        "num": 2.34,
    })


def main():
    client = MongoClient('192.168.1.102', 27017)
    db = client['mytest']
    collection = db['time']

    # collection.insert({
    #     "time": datetime.now()
    # })

    collection.insert({
        "time":datetime.strptime("2017-01-28", "%Y-%m-%d")
    })

if __name__ == '__main__':
    main()
