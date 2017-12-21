#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app01.backend import redis_conn
from app01 import models

class DataHandler(object):
    def __init__(self, setting, redis):
        self.setting = setting
        if redis:
            self.redis = redis_conn.redis_conn(setting)

    def load_service_data_and_calulating(self,host_ojb,trigger, redis_obj):
        self.redis = redis_obj

        # 用于存放每一个 Trigger expressions 的结果，Trigger expressions的结果只可能是True或者False
        # 再将此列表与每个Trigger expressions中的Logic type，组合成一个字符串，如：'True and False or True'
        # 通过 eval('True and False or True')就可得出，最终的报警状态。
        calc_sub_res_list = []



        print(trigger)



        pass
