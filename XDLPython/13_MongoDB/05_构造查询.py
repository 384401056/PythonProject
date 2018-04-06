#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import json
from time import time
from datetime import datetime
import re

def find_and_findone():
    """find和findone的区别"""
    client = MongoClient('192.168.1.102', 27017)
    db = client['mytest']
    collection = db['user']
    u1 = collection.find({"age": 22})
    u2 = collection.find_one({"age": 22})
    print(type(u1))
    print(type(u2))


def page():
    """分页"""
    client = MongoClient('192.168.1.102', 27017)
    db = client['mytest']
    collection = db['user']

    page_number = 500  # 第几页
    page_size = 10  # 每页多少条
    page_count = 0  # 共多少页

    # 判断总页数，是否为整数。不时则加一页
    if collection.find().count() % page_size == 0:
        page_count = collection.find().count() // page_size  # 共多少页
    else:
        page_count = collection.find().count() // page_size + 1

    ret = collection.find().skip((page_number - 1) * page_size).limit(page_size)

    for i in ret:
        print(i)

    print("page_number:", page_number)
    print("page_count:", page_count)


def sort_by_key():
    """排序"""
    client = MongoClient('192.168.1.102', 27017)
    db = client['mytest']
    collection = db['user']

    # 1 为升序排列，而-1是用于降序排列
    ret = collection.find().limit(10).sort("age", 1)

    print(type(ret))
    for i in ret:
        print(i)


def fillter_column():
    """投影返回限制字段"""
    client = MongoClient('192.168.1.102', 27017)
    db = client['mytest']
    collection = db['user']
    ret = collection.find({"name": "屈芳"}, {"_id": 1, "address": 1})

    for i in ret:
        print(i)


def main():
    client = MongoClient('192.168.1.102', 27017)
    db = client['mytest']
    collection = db['user']
    ret = collection.find({"name": re.compile('^周')})

    for i in ret:
        print(i)

    # collection = db['categories']
    #
    # collection.insert({
    #     "name":"Gardening Tools",
    # })

    # collection = db['products']
    # collection_categry = db['categories']
    #
    # collection.insert({
    #     "name":"Wheelbarrow",
    #     "primary_category": collection_categry.find_one({"name":"Gardening Tools"})["_id"]
    # })

if __name__ == '__main__':
    main()
