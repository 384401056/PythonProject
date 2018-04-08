#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from MongoDBConn import MongoDBConn

if __name__ == '__main__':
    client = MongoDBConn(db_name='mytest', set_name='numbers')
    numbers = client.getSet()

    for i in range(20001):
        numbers.save({"num":i})

    # user_list = [
    #     {
    #         'name': 'Lily',
    #         'age': 10
    #     },
    #     {
    #         'name': 'Jams',
    #         'age': 20
    #     },
    # ]

    # users.insert_many(user_list)

    # rets = users.find({"name":'Jams'})

    # print(type(rets))

    # for ret in rets:
    #     print(ret)