#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import json
import time

from CrazyMonitor import settings


class DataStore(object):

    def __init__(self, client_id, service_name, data, redis_conn):
        """
        :param client_id:
        :param service_name:
        :param data:
        :param redis_conn:
        """
        self.client_id = client_id
        self.service_name = service_name
        self.data = data
        self.redis_conn = redis_conn
        self.process_and_save()

    def process_and_save(self):
        """将数据处理并存入redis中"""

        # 如果数据是有效的
        if self.data['status'] == 0:
            for key, data_series_val in settings.STATUS_DATA_OPTIMIZATION.items():

                # 生成存入redis中的key,每个服务有如下4类数据:
                # StatusData_1_LinuxCPU_latest
                # StatusData_1_LinuxCPU_10mins
                # StatusData_1_LinuxCPU_30mins
                # StatusData_1_LinuxCPU_60mins

                data_series_key_in_redis = 'StatusData_%s_%s_%s' % (self.client_id, self.service_name, key)

                # 根据key从redis中取出，此类数据的最后一条。
                last_point_from_redis = self.redis_conn.lrange(data_series_key_in_redis, -1, -1)

                # 如果没有最后一条数据，则存入一条data为空，但有时间戳的数据。这条特殊的数据可以在以
                # 后用来判断是否到时间，存入不同类型的数据。这里存入使用的是redis的list数据类型，是有序的。
                # 而且用的是rpush,所以新数据都是加在右边的。
                if not last_point_from_redis:
                    self.redis_conn.rpush(data_series_key_in_redis, json.dumps([None, time.time()]))

                # 如果是latest类型，即key为：_latest
                # 则直接存入redis中。这里存入使用的是redis的list数据类型，所以是有序的。
                if data_series_val[0] == 0:
                    self.redis_conn.rpush(data_series_key_in_redis, json.dumps([self.data, time.time()]))

                # 如果是其它类型。即key为：_10mins，_30mins，_60mins
                else:
                    # 取出最后一条此类型的数据内容,经过上面的处理，这里是一定能取到数据的。lrange取出的是列表，就算只有一条也要加[0]
                    last_point_data, last_point_save_time = json.loads(self.redis_conn.lrange(data_series_key_in_redis, -1, -1)[0])

                    # 如果当前时间 - 最后一条数据的时间 > 配置文件中的间隔时间。
                    if time.time() - last_point_save_time > data_series_val[0]:
                        # 生成取出redis中数据的key， 此处取的都是latest类型的。
                        last_data_key_in_redis = 'StatusData_%s_%s_latest' % (self.client_id, self.service_name)

                        # 取出符合 optimization_interval 时间间隔的实时数据
                        data_set = self.get_data_slice(last_data_key_in_redis, data_series_val[0])

                        if len(data_set) > 0:
                            print('key:', key, 'data_set_len:', len(data_set))
                            optimizaed_date = self.get_optimizaed_data(data_series_key_in_redis, data_set)

                            # 如果数据不为空
                            if optimizaed_date:
                                self.save_optimized_data(data_series_key_in_redis, optimizaed_date)

                # 如果reids中同一key的值的数量，超过了settings文件中的配置数量，就删除一条最早的数据
                if self.redis_conn.llen(data_series_key_in_redis) >= data_series_val[1]:
                    # lpop从左边开始删除，也就是最早的数据
                    self.redis_conn.lpop(data_series_key_in_redis)
        else:
            print('Report Data is invalid')
            raise ValueError

    def get_data_slice(self, latest_data_key, optimization_interval):
        """
        取出符合 optimization_interval 时间间隔的实时数据
        也就是取出了，实时数据中的 10min 30min, 60min 的数据
        """

        now_time = time.time()
        all_real_data = self.redis_conn.lrange(latest_data_key, 1, -1)
        data_set = []
        for item in all_real_data:
            # 将redis中的每个数据转为对象。只要是从redis中取出的数据，要立即转成对象。
            # 这步很关键。否则后面对data_set的操作就有问题了。
            data = json.loads(item)
            if len(data) == 2:
                servcice_data, last_save_time = data
                # 如果数据存储时间在 optimization_interval 的范围之内。则取出放入data_set中。
                if now_time - last_save_time <= optimization_interval:
                    data_set.append(data)

        return data_set

    def get_optimizaed_data(self, data_series_key_in_redis, data_set):
        """
        将传入的数据集合，解析成10min, 30min, 60min 的新格式,即每个key对应一个列表。
        列表中为多个数据的形式。
        """
        service_data_keys = data_set[0][0].keys()  # 取出数据集合中的第一条数据的第一个列表（也就是纯数据）的keys
        first_service_data_point = data_set[0][0]  # 取出数据集合中的第一条数据的第一个列表的数据
        # print('===>', service_data_keys)

        # 创建新格式的字典。
        optimized_dict = {}

        # 如果不是特殊的有字集合的数据（如：网卡）
        if 'data' not in service_data_keys:
            # 生成新格式的字典
            for key in service_data_keys:
                optimized_dict[key] = []

            tmp_data_dict = copy.deepcopy(optimized_dict)  # 深度拷贝一份新格式的临时字典

            # 循环data_set, 生成新格式的临时字典
            for service_data_item, last_time_item in data_set:
                for server_index, v in service_data_item.items():
                    tmp_data_dict[server_index].append(round(float(v), 2))
                    """
                    生成的新格式，类似于这样的。
                    {
                        'nice': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                        'user': [3.04, 3.04, 3.04, 3.04, 3.04, 3.04, 3.04, 3.04, 3.04, 3.04], 
                        'idle': [96.8, 96.8, 96.8, 96.8, 96.8, 96.8, 96.8, 96.8, 96.8, 96.8], 
                        ....
                    }
                    """
            # 通过对临时字典的再次重组，生成最终的新格式。
            for service_key, v_list in tmp_data_dict.items():
                avg_res = self.get_average(v_list)  # 计算平均值
                max_res = self.get_max(v_list)  # 计算最大值
                min_res = self.get_min(v_list)  # 计算最小传值
                mid_res = self.get_mid(v_list)  # 计算中间值

                optimized_dict[service_key] = [avg_res, max_res, min_res, mid_res]

        # 如果是有字集合的数据（如：网卡）
        else:
            for service_item_key, v_dic in first_service_data_point['data'].items():
                optimized_dict[service_item_key] = {}

                # 生成新格式的字典
                for k2, v2 in v_dic.items():
                    optimized_dict[service_item_key][k2] = []

            tmp_data_dict = copy.deepcopy(optimized_dict)
            # 如果不为空
            if tmp_data_dict:
                for service_data_item, last_time_item in data_set:
                    # [{'status': 0, 'data': {'lo': {'t_in': 74, 't_out': 35}, 'eth0': {'t_in': 73, 't_out': 85}, 'docker': {'t_in': 95, 't_out': 89}}} 1513487783.8357575]

                    for service_index, val_dict in service_data_item['data'].items():
                        # {'lo': {'t_in': 74, 't_out': 35}, 'eth0': {'t_in': 73, 't_out': 85}, 'docker': {'t_in': 95, 't_out': 89}}

                        for server_item_sub_key, val in val_dict.items():
                            # {'t_in': 74, 't_out': 35}

                            tmp_data_dict[service_index][server_item_sub_key].append(round(float(val),2))
                            # {'lo':{
                            #     't_in': [74.0, 74.0, 74.0, 74.0, 74.0, 2.0, 2.0, 2.0, 2.0, 2.0],
                            #     't_out': [35.0, 35.0, 35.0, 35.0, 35.0, 46.0, 46.0, 46.0, 46.0, 46.0],
                            # }}
                            # 通过对临时字典的再次重组，生成最终的新格式。

                for service_key, v_dict in tmp_data_dict.items():
                    for service_sub_key, v_list in v_dict.items():
                        avg_res = self.get_average(v_list)  # 计算平均值
                        max_res = self.get_max(v_list)  # 计算最大值
                        min_res = self.get_min(v_list)  # 计算最小传值
                        mid_res = self.get_mid(v_list)  # 计算中间值
                        optimized_dict[service_key][service_sub_key] = [avg_res, max_res, min_res, mid_res]

            # 如果为空
            else:
                print('')

        # print('optimized empty dic', optimized_dict)
        return optimized_dict

    def save_optimized_data(self, data_series_key_in_redis, optimizaed_data):
        # 将数据存入redis.只加上了时间，没有了status。
        self.redis_conn.rpush(data_series_key_in_redis, json.dumps([optimizaed_data, time.time()]))

    def get_average(self, data_set):
        """对传入的列表求平均值"""
        return round(float(sum(data_set)) / len(data_set), 2)

    def get_max(self, data_set):
        """对传入的列表求最大值"""
        return max(data_set)

    def get_min(self, data_set):
        """对传入的列表求最小值"""
        return min(data_set)

    def get_mid(self, data_set):
        """对传入的列表求中间值"""
        data_set.sort() # 排序
        return data_set[int(len(data_set)/2)]


def main():
    pass


if __name__ == '__main__':
    main()
