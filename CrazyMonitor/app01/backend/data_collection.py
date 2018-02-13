#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
from app01 import models
from CrazyMonitor import settings
from django.core.serializers import serialize


class Collection(object):
    """
    数据获取
    """

    def __init__(self, redis_conn):
        self.redis = redis_conn

    def get_all_hostgroup(self):
        """
        获取所有的主机组信息.
        :return:
        """
        ret = {}
        try:
            groups_obj = models.HostGroup.objects.values('id', 'name', 'memo')
            ret['data'] = list(groups_obj)
            ret['status'] = 1

            for item in ret['data']:
                item['services'] = self.get_group_services(item['id'])
                item['trigger'] = self.get_group_triggers(item['id'])
        except Exception as ex:
            print(ex)
            ret['err'] = str(ex)
        finally:
            return ret

    def get_group_services(self, group_id):
        """
        通过group的id获取组内包含的监控服务
        :param group_id:
        :return:
        """
        ret = []
        # 通过id获取到单个HostGroup
        groups_obj = models.HostGroup.objects.get(id=group_id)
        for item in groups_obj.templates.select_related():
            for service in item.services.select_related():
                ret.append({
                    'name':service.name,
                    'interval':service.interval,
                    'plugin_name':service.plugin_name,
                    # 'service_index':[],# 存储service对应的指标
                    'memo':service.memo,
                })
                # 获取service对应的指标。
                # for index in service.items.select_related():
                #     print(index)
        return ret

    def get_host_services(self,host_id):
        """
        通过主机id获取主机本身配置的监控服务
        :param host_id:
        :return:
        """
        ret = []
        host_obj = models.Host.objects.get(id=host_id)
        for item in host_obj.templates.select_related():
            for service in item.services.select_related():
                ret.append({
                    'name': service.name,
                    'interval': service.interval,
                    'plugin_name': service.plugin_name,
                    # 'service_index':[],# 存储service对应的指标
                    'memo': service.memo,
                })
        return ret

    def get_group_triggers(self, group_id):
        """
        通过group的id获取组内templates中包含的触发器和触发报警条件
        :param group_id:
        :return:
        """
        ret = []
        # 通过id获取到单个HostGroup
        groups_obj = models.HostGroup.objects.get(id=group_id)
        for item in groups_obj.templates.select_related():
            for trigger in item.trigger.select_related():
                # 获取触发器
                trg_ret = {
                    'name': trigger.name,
                    'serverity': trigger.serverity,
                    'enable': trigger.enable,
                    'memo': trigger.memo,
                    'expression': []
                }
                #　获取触发器对应的触发条件
                for expression in trigger.triggerexpression_set.select_related():
                    trg_ret['expression'].append({
                        'service_index': expression.service_index.name,
                        'data_clac_func': expression.data_clac_func,
                        'operator_type': expression.operator_type,
                        'threshold': expression.threshold,
                    })

                # 将组装出的数据加入ret列表。
                ret.append(trg_ret)
        return (ret)

    def get_hosts_by_groupid(self,group_id):
        """
        获取指定组编号的主机列表
        :param group_id:
        :return:
        """
        ret = {}
        try:
            hosts_obj = models.Host.objects.filter(host_group__id=group_id).values(
                'id','name','ip_addr','status', 'memo', 'host_group__name'
            )
            ret['data'] = list(hosts_obj)
            ret['status'] = 1

            for item in ret['data']:
                group_service = self.get_group_services(group_id) # 获取HostGroup的监控服务。
                host_service = self.get_host_services(item['id']) # 获取Host本身的监控服务。
                # 去重HostGroup的监控服务与Host本身的监控服务
                [group_service.append(service_item) for service_item in host_service if service_item not in group_service]

                item['services'] = group_service
                item['trigger'] = self.get_group_triggers(group_id)


        except Exception as ex:
            print(ex)
            ret['err'] = str(ex)
        finally:
            return ret


    def get_redis_data_by_hostid(self,host_id,flag):
        '''
        根据host_id获取主机最新的监控数据。host_id是客户端id, flag: 如果为0则取出所有的，如果为-1则取出最新
        :param host_id:
        :param flag: 如果为0则取出所有的，如果为-1则取出最新
        :return:
        '''
        ret = {}
        try:
            host_obj = models.Host.objects.filter(id = host_id).values('host_group__id').first()
            # 获取Group的服务和主机的服务，进行去重后返回。
            group_services = self.get_group_services(host_obj['host_group__id'])
            host_services = self.get_host_services(host_id)
            [host_services.append(service) for service in group_services if service not in host_services]

            for service in host_services:
                temp = {}
                for key, value in settings.STATUS_DATA_OPTIMIZATION.items():
                    key_in_redis = 'StatusData_%s_%s_%s' % (host_id, service['name'], key)
                    real_data = self.redis.lrange(key_in_redis, flag, -1)# 取出最新的与key_in_redis对应的数据
                    # print(real_data)
                    data = self.format_redis_data(real_data)
                    # print(data)
                    temp[key] = data
                ret[service['name']] = temp
            return ret
        except Exception as ex:
            print(ex)
            ret['err'] = str(ex)
        finally:
            return ret


    def format_redis_data(self, redis_data):
        """
        将从redis中取出的数据转为对象并格式化日期
        :param redis_data:
        :return:
        """
        ret = []
        for item in redis_data:
            # 将redis中的每个数据转为对象。只要是从redis中取出的数据，要立即转成对象。
            data = json.loads(item)
            data[1] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data[1]))
            if data:
                ret.append(data)
        return ret

















