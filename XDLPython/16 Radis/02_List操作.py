#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import redis
import time


def main():
    redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379 ,db = 0)
    r = redis.Redis(connection_pool=redis_pool)

    # 将一个列表存入redis,或在已经存在的列表最左边加入元素
    # r.lpush('cars', 'Ford', 'Honda', 'Benz', 'BMW')

    # r.lpush('cars', 'Audi')

    # print(r.lrange('cars', 0, -1)) # 分片获取元素, 0是开始，-1是结束
    # print(r.lrange('cars', -3, -1)) # 分片获取元素, 0是开始，-1是结束



    # for i in range(100):
    #     user_dict = {}
    #     user_dict['user_%s' % i] = {'name':'Jims_%s' % i, 'age':20+i}
    #     r.lpush('User', json.dumps(user_dict))

    data_range = r.lrange('User', -10, -1)

    data = [json.loads(item) for item in data_range]

    print(data)

    # 在已经存在列表右边加入元素
    # r. rpush('cars', 'Beijing')
    # print(r.lrange('cars', 0, -1))

    # r.delete('StatusData_1_LinuxCPU_latest')

    # data = {"nice": "0.00", "status": 0, "iowait": "0.00", "user": "3.04", "steal": "0.00", "idle": "96.80",
    #         "system": "0.17"}

    # data_ = {"nice": "0.00", "status": 0, "iowait": "0.00", "user": "3.04", "steal": "0.00", "idle": "96.80",
    #         "system": "0.17"}

    # for i in range(5):
    #     r.rpush('StatusData_1_LinuxCPU_latest', json.dumps([data, time.time()]))
    #     time.sleep(1)

    # all_real_data = r.lrange('StatusData_1_LinuxCPU_latest', 0, -1)
    # data_set = []
    # for item in all_real_data:
    #     data = json.loads(item)
    #     data_set.append(data)

    # list_first = json.loads(data_set[0]) # redis中的取出的数据要转成对象后才能使用python的方式进行操作。
    # print(list_first[0])

    # item1, item2 = data_set[0]
    # print(item1)
    # print(item2)
    # opt_dict = {}

    # service_data_keys = data_set[0][0].keys()
    # # print(service_data_keys)
    # for key in service_data_keys:
    #     opt_dict[key] = []

    # for data_item, last_time in data_set:
    #     for server_index, v in data_item.items():
    #         opt_dict[server_index].append(round(float(v),2))
    # print(opt_dict)


if __name__ == '__main__':
    main()
