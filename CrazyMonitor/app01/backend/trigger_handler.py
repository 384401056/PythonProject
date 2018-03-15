#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,django
from app01.backend import redis_conn
import pickle,time

class TriggerHandler(object):

    def __init__(self, setting):
        self.setting = setting
        self.redis = redis_conn.redis_conn(self.setting)
        self.alert_counters = {} # 记录每个action的触发报警次数.


    def start_watch(self):
        """
        循环订阅redis发来的报警信息
        :return:
        """
        radio = self.redis.pubsub() # 订阅reids
        radio.subscribe(self.setting.TRIGGER_CHAN) # 设置订阅的频道.
        radio.parse_response()  # 订阅开始
        print('******************* Start listening a new trigger*****************')
        self.trigger_count = 0
        while True:
            msg = radio.parse_response()
            self.trigger_consume(msg)



    def trigger_consume(self, msg):
        """
        对信息进行处理。
        :param msg:
            msg的信息格式如下：
            [
                b'message',
                b'trigger_event_channal',
                b'\x80\x03}q\x00(X\x07\x00\x00\x00host_i'
            ]
        :return:
        """
        self.trigger_count += 1
        print('******************* Got a trigger msg: %s *****************' % msg[0])
        trigger_msg = pickle.loads(msg[2])

        # 打印出报警信息。
        for item in trigger_msg.items():
            print(item)

        # 真正处理报警的动作在ActionHandler类中去完成，比如发送短信、邮件等方式。
        action = ActionHandler(trigger_msg, self.alert_counters)
        action.trigger_process()




class ActionHandler(object):
    """负责把达到报警条件的 trigger 进行分析，并根据action表中的配置来进行报警"""
    def __init__(self, trigger_msg, alert_counters):
        pass


    def trigger_process(self):
        pass
