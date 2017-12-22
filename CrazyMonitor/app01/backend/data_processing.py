#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app01.backend import redis_conn
from app01 import models
import operator # 一个 "功能性" 的标准操作符接口
import pickle

class DataHandler(object):
    def __init__(self, setting, redis):
        self.setting = setting
        if redis:
            self.redis = redis_conn.redis_conn(setting)

    def load_service_data_and_calulating(self,host_ojb,trigger, redis_obj):
        """
        加载触发器数据并进行计算.
        :param host_ojb:
        :param triggers:
        :param redis_obj:
        :return:
        """
        self.redis = redis_obj
        calc_sub_res_list = [] # 表达式的计算结果列表
        positive_expressions = [] # 报警的expression列表
        expression_res_string = '' # 最终多个表达式的结果，和拼上关系运算符后的字符串。

        # 用于存放每一个 Trigger expressions 的结果，Trigger expressions的结果只可能是True或者False
        # 再将此列表与每个Trigger expressions中的Logic type，组合成一个字符串，如：'True and False or True'
        # 通过 eval('True and False or True')就可得出，最终的报警状态。
        for expression in trigger.triggerexpression_set.select_related().order_by('id'):
            print('Expression:', expression)
            expression_process_obj = ExpressionProcess(self, host_ojb, expression)

            # 按照TriggerExpression中的参数,从redis中取出多长时间的数据,进行计算和阀值报警的判断。
            # 返回的是一个字典或者False
            single_expression_ret = expression_process_obj.process()

            # 如果返回的不是False
            if single_expression_ret:
                calc_sub_res_list.append(single_expression_ret)

                # 如果关系运算符存在，则说明还有判断条件
                if single_expression_ret['expression'].logic_type:
                    expression_res_string += str(single_expression_ret['calc_res'])+ ' ' \
                                             + single_expression_ret['expression'].logic_type + ' '
                else:
                    expression_res_string += str(single_expression_ret['calc_res'])
                    pass

                # 把报警结果为True的expression提取出来，这样才知道哪些指标是报警的。
                if single_expression_ret['calc_res']:
                    positive_expressions.append(expression)

        print('Whole trigger res:', trigger.name, expression_res_string)

        if expression_res_string:
            # 计算多个表达式值的最后结果。
            trigger_res = eval(expression_res_string)
            print('whole trigger res:', trigger_res)

            # 如果最终结果为True,说明要触发报警了。
            if trigger_res:
                self.trigger_notifier(host_ojb, trigger.id, positive_expressions, self.redis)


    def trigger_notifier(self, host_obj, trigger_id, positive_expressions, redis_obj=None, msg=None):
        """
        执行报警..
        :param host_obj:
        :param trigger_id:
        :param positive_expressions:
        :param redis:
        :return:
        """
        if redis_obj:
            self.redis = redis_obj

        msg_dict= {
            'host_id':host_obj.id,
            'trigger_id':trigger_id,
            'positive_expressions': positive_expressions,
            'msg':msg
        }

        print("Trigger_Notifier:", host_ojb, trigger, pickle.dumps(msg_dict))

        # self.redis.publish(self.setting.TRIGGER_CHAN, pickle.dumps(msg_dict)) # reids之发布。


class ExpressionProcess(object):
    """
    通过触发器表达式，进行计算。(只是计算一条表达式的结果)
    """
    def __init__(self, main_ins, host_obj, expression_obj):
        self.host_obj = host_obj
        self.expression = expression_obj
        self.main_ins = main_ins

        # 生成redis中的key.用此key来
        self.service_redis_key = 'StatusData_%s_%s_latest' % (host_obj.id, expression_obj.expression.service.name)
        # 取数据的时间范围.这个参数存在了redis中,单位是分钟.
        self.time_range = expression_obj.data_clac_args.split(',')[0]



    def process(self):
        """
        根据时间，从redis的 StatusData_x_x_latest 中取出一段时间的数据
        :return:
        """
        data = self.load_data_from_redis()

        # 通过反射，获取要进行计算的函数名
        func_name = 'get_%s' % self.expression.data_clac_func
        data_calc_func = getattr(self, func_name)
        single_expression_calc_ret = data_calc_func(data)  # 计算单个表达式的结果。

        print('single_expression_calc_ret:',single_expression_calc_ret)

        # 如果单个结果不为空.
        if single_expression_calc_ret:
            res_dic = {
                'calc_res':single_expression_calc_ret[0], # 判断是否报警的结果
                'calc_res_val:': single_expression_calc_ret[1], # 用于判断结果的值（也就是计算出来的值）
                'expression_obj': self.expression_obj,
                'service_item': single_expression_calc_ret[2]
            }

            print('res_dic:', res_dic)
            return res_dic
        else:
            return False



    def load_data_from_redis(self):
        """
        从redis中取出符合要求的数据。
        :return:
        """
        time_in_sec = int(self.time_range)*60 # 按分钟取
        # 多加一分钟的数据，并用此数除以服务的监控间隔（多久发一次数据），就可以得到大概要取多少条数据。
        approximate_data_points = (time_in_sec+60) / self.expression.service.interval
        print('approximate_data_points:', approximate_data_points)

        # 从redis中取出的原始数据，从最后一个（-1)开始，往前取 approximate_data_points 个
        data_range_raw = self.main_ins.redis.lrange(self.service_redis_key, -approximate_data_points, -1)

        # 获得大概的数据列表。
        approximate_data_range = [json.loads(item) for item in data_range_raw] # 列表推导式,返回的数据要进行返序列化处理。

        data_range = [] # 用于保存精确数据

        # 对大概数据进行分析，如果时间在范围内的就存入 data_range
        for point in approximate_data_range:
            val, saving_time = point
            if time.time() - saving_time < time_in_sec: # 如果数据的时间在范围内.
                data_range.append(point)

        return data_range

    def get_avg(self, data_set):
        """
        对传入的data_set数据，进行平均值计算。process方法调用此类方法
        :param data_set:
        :return:
        """
        clean_data_list = []  # 存储普通监控服务的数据
        clean_data_dic = {}  # 存储有子集的监控服务的数据。
        for point in data_set:
            val, save_time = point

            # 确保取到的是有效数据，而不是库里的第一条空值数据。
            if val:

                # 如果不是特殊的有子集的数据。
                if 'data' not in val.keys():
                    # 通过表达式对象expression，找出触发器中的实际监控指标名(如:iowait, idle...)对应的值。
                    # 并加入 clean_data_list 中
                    clean_data_list.append(val[self.expression.service_index.key])

                else:
                    for k,v in val['data'].items():
                        if k not in clean_data_dic.keys():
                            clean_data_dic[k] = [] # 对data中的每个字项生成一个列表。
                        clean_data_dic[k].append(v[self.expression.service_index.key]) # 在列表中存入监控指标的值。

            # 如果普通数据列表不为空
            if clean_data_list:
                # 将列表中的值转为float
                clean_data_list = [float(i) for i in clean_data_list]

                # 计算平平均值
                # avg_res = 0 if sum(clean_data_list) == 0 else sum(clean_data_list)/len(clean_data_list)
                avg_res = sum(clean_data_list)/len(clean_data_list)

                return [self.judge(avg_res), avg_res, None] #
            else:
                pass

    def get_max(self):
        pass

    def get_hit(self):
        pass


    def get_last(self):
        pass

    def judge(self, value):
        """
        判断计算出来的值（平均值或者最大值等）是否超过阀值。(这只是一条表达的判断结果)
        :param value: 计算出来的值。
        :return: 是否报警.
        """

        # 获取判断大于,等于，小于的操作符，这里使用了operator模块。
        # 通过反射取出对应operator中的操作函数,进行阀值的比较.(注意：数据库中的操作字符要与operator中的函数名对应)
        calc_func = getattr(operator, self.expression.operator_type)

        return calc_func(value, self.expression.threshold) # 比较两个值并返回



















