#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import json

def func01():
    redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1)
    r = redis.Redis(connection_pool=redis_pool)
    last_point_data, last_point_save_time = json.loads(r.lrange('StatusData_1_LinuxCPU_latest', -1, -1)[0])
    # print(last_point_data, last_point_data)
    # for item in data_list:
    #     data= json.loads(item)
    #     last_point_data, last_point_save_time = data
    #     print(last_point_data, last_point_save_time)
    # last_point_data, last_point_save_time = json.loads()
    #
    # print(last_point_data,last_point_save_time)

    key_list = []
    for key, val in last_point_data.items():
        key_list.append(key)

    print(key_list[int(len(key_list) / 2)])

    # 将一个列表存入redis,或在已经存在的列表最左边加入元素
    # r.lpush('cars', 'Ford', 'Honda', 'Benz', 'BMW')
    # print(r.lrange('cars', 0, -1)) # 分片获取元素 0是开始，-1是结束
    #
    # r.lpush('cars', 'Audi')

    # 在已经存在列表右边加入元素
    # r. rpush('cars', 'Beijing')
    # print(r.lrange('cars', 0, -1))

    # r.delete('car')
    # r.delete('StatusData_1_LinuxNIC_latest')

    # data = {"nice": "0.00", "status": 0, "iowait": "0.00", "user": "3.04", "steal": "0.00", "idle": "96.80",
    #         "system": "0.17"}
    #
    # for i in range(5):
    #     r.rpush('StatusData_1_LinuxCPU_latest', json.dumps([data, time.time()]))
    #     time.sleep(1)

    # all_real_data = r.lrange('StatusData_1_LinuxCPU_latest', 0, -1)
    # data_set = []
    # for item in all_real_data:
    #     data = json.loads(item)
    #     data_set.append(data)
    # opt_dict = {}
    # service_data_keys = data_set[0][0].keys()
    # # print(service_data_keys)
    # for key in service_data_keys:
    #     opt_dict[key] = []
    #
    # for data_item, last_time in data_set:
    #     for server_index, v in data_item.items():
    #         opt_dict[server_index].append(round(float(v), 2))
    # print(opt_dict)

    # 真实的网卡数据格式。
    # data_type_2 = {
    #     'status': 0,
    #     'data': {
    #         'lo': {'t_in': random.randint(0, 100), 't_out': random.randint(0, 100), },
    #         'eth0': {'t_in': random.randint(0, 100), 't_out': random.randint(0, 100), },
    #         'docker': {'t_in': random.randint(0, 100), 't_out': random.randint(0, 100), },
    #     }
    # }
    #
    # for i in range(5):
    #     r.rpush('StatusData_1_LinuxNIC_latest', json.dumps([data_type_2, time.time()]))
    #     time.sleep(1)

    # all_real_data = r.lrange('StatusData_1_LinuxCPU_latest', 0, -1)
    # data_set = []
    # for item in all_real_data:
    #     data = json.loads(item)
    #     data_set.append(data)
    # opt_dict = {}
    #
    # for key, val in data_set:
    #     print(key, val)

    # first_service_data_point = data_set[0][0]
    # for service_item_key, v_dic in first_service_data_point['data'].items():
    #     opt_dict[service_item_key] = {}
    #     for k2, v2 in v_dic.items():
    #         opt_dict[service_item_key][k2] = []
    #
    # for k,v in opt_dict.items():
    #     print(k)
    #     print(v)

    # for service_data_item, last_time_item in data_set:
    #     for service_index, val_dict in service_data_item['data'].items():
    #         for server_index_sub_key, val in val_dict.items():
    #             opt_dict[service_index][server_index_sub_key].append(round(float(val), 2))
    #
    # for service_key, v_dict in opt_dict.items():
    #     print(service_key, v_dict)
    #     for service_sub_key, v_list in v_dict.items():
    #         print(service_sub_key, v_list)


def main():
    print(eval('True and False'))
    # func01()


if __name__ == '__main__':
    main()
