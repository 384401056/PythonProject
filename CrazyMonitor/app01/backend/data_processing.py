#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app01.backend import redis_conn
from app01 import models
import operator  # 一个 "功能性" 的标准操作符接口
import pickle
import time
import json


class DataHandler(object):
    def __init__(self, setting, connect_redis):
        self.setting = setting
        self.poll_interval = 0.5
        self.config_update_interval = 120 #　更新字典的时间间隔
        self.config_last_loading_time = time.time() #　最后一次获取监控配置字典的时间

        # 主机最后一次上传数据的时间，有没有超过他应该上报的间隔。此字典用来存主机的相关信息。
        self.global_monitor_dic = {}
        self.exit_flag = False

        # 如果为True,重新生成redis连接池。
        if connect_redis:
            self.redis = redis_conn.redis_conn(setting)

    def load_service_data_and_calulating(self, host_ojb, trigger, redis_obj):
        """
        加载触发器数据并进行计算.
        :param host_ojb:
        :param triggers:
        :param redis_obj:
        :return:
        """
        self.redis = redis_obj
        calc_sub_res_list = []  # 表达式的计算结果列表
        positive_expressions = []  # 报警的expression列表
        expression_res_string = ''  # 最终多个表达式的结果，和拼上关系运算符后的字符串。

        # 用于存放每一个 Trigger expressions 的结果，Trigger expressions的结果只可能是True或者False
        # 再将此列表与每个Trigger expressions中的Logic type，组合成一个字符串，如：'True and False or True'
        # 通过 eval('True and False or True')就可得出，最终的报警状态。

        print('======================== start calulating ===============================')
        # print('Triggers:', trigger)

        for expression in trigger.triggerexpression_set.select_related().order_by('id'):  # 按降序来排。
            print('Expression:', expression)
            expression_process_obj = ExpressionProcess(self, host_ojb, expression)

            # 按照TriggerExpression中的参数,从redis中取出多长时间的数据,进行计算和阀值报警的判断。
            # 返回的是一个字典或者False
            single_expression_ret = expression_process_obj.process()

            print('single_expression_ret:', single_expression_ret)

            # 如果返回的不是False
            if single_expression_ret:
                calc_sub_res_list.append(single_expression_ret)

                # 如果关系运算符存在，则说明还有判断条件
                if single_expression_ret['expression_obj'].logic_type:
                    expression_res_string += str(single_expression_ret['calc_res']) + ' ' \
                                             + single_expression_ret['expression_obj'].logic_type + ' '
                else:
                    expression_res_string += str(single_expression_ret['calc_res'])
                    pass

                # 把报警结果为True的expression提取出来，这样才知道哪些指标是报警的。
                if single_expression_ret['calc_res']:
                    positive_expressions.append(expression)

        # print('expression_res_string:', expression_res_string)

        if expression_res_string:
            # 计算多个表达式值的最后结果。
            trigger_res = eval(expression_res_string)

            # 如果最终结果为True,说明要触发报警了。
            if trigger_res:
                self.trigger_notifier(host_ojb, trigger.id, positive_expressions, self.redis)
        else:
            print('===========>>>No Notifiler')

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

        msg_dict = {
            'host_id': host_obj.id,
            'trigger_id': trigger_id,
            'positive_expressions': positive_expressions,
            'msg': msg,
            'datetime:': time.time()
        }

        # 由于positive_expressions是数据库对象，所以不能用json序列化，只能用pickle
        pk_str = pickle.dumps(msg_dict)
        # print(pk_str)
        # reids发布订阅。第一个参数是频道的名称，第二个参数是发布的消息。
        self.redis.publish(self.setting.TRIGGER_CHAN, pk_str)
        print('===========>>>Redis publish Trigger_Notifier:', pickle.loads(pk_str))

    def looping(self):
        """
        监控主机是否存活
        :return:
        """
        self.update_or_load_config()
        count = 0
        while not self.exit_flag:
            print('looping %s'.center(50, '-') % count)
            count += 1

            # 如果当前时间减最后一次获取监控配置字典的时间大于120秒，则再获取一次数据字典.
            # 也就是定时更新监控配置字典
            if time.time() - self.config_last_loading_time >= self.config_update_interval:
                print("need update configs....")
                self.update_or_load_config()

            if self.global_monitor_dic:
                # 遍历全局字典
                for host, config_dict in self.global_monitor_dic.items():

                    for service_id ,val in config_dict['services'].items(): # 循环所有要监控的服务。
                        service_obj, last_monitor_time = val

                        # 如果当前时间减最后监控的时间大于等于服务本身的监控间隔，
                        # 也就是说，如果服务器的监控间隔为60秒的话，在这60秒的时间内就没必要再判断了。就直接让
                        # last_moniter_time = ti
                        if time.time() - last_monitor_time >= service_obj.interval:
                            self.global_monitor_dic[host]['services'][service_id][1] = time.time()

                            self.data_point_validation(host, service_obj) # 检测此服务汇报的数据。
                        else:
                            next_monitor_time = time.time()-last_monitor_time-service_obj.interval



                pass

    def data_point_validation(self,host, service_obj):











        pass

    def update_or_load_config(self):
        """
        从数据库获取所有主机的监控配置.生成全局的监控配置字典self.global_monitor_dic
        :return: True
        """
        all_enable_hosts = models.Host.objects.filter(status=1)  # 取出所有启用的主机信息
        for host in all_enable_hosts:
            if host not in self.global_monitor_dic.keys():
                # 以主机名为key,建立新字典。
                self.global_monitor_dic[host] = {'services': {}, 'triggers': {}}
                # self.global_monitor_dic = {
                #     'host1':{
                #         'services':{
                #             '1':[service_obj, 0],
                #             '2':[service_obj, 0],
                #         },
                #         'triggers':{
                #             '1': trigger_obj,
                #             '2': trigger_obj,
                #         }
                #     }
                #     .....
                # }
                # 这个字典的最终格式如上，下面的for循环就是为了拼出这个格式。

            for group in host.host_group.select_related():  # 取出主机信息只关联的主机组，并循环每个组
                service_list = []
                trigger_list = []

                for template in group.templates.select_related():  # 取出主机组信息中关联的模板，并循环.
                    service_list.extend(template.services.select_related())  # 取出单个模板中的服务加入service_list
                    trigger_list.extend(template.trigger.select_related())  # 取出单个模板中的触发器加入trigger_list

                for service in service_list:
                    # 如果global_monitor_dic中没有些services的数据，就将些service加入数据字典中
                    if service.id not in self.global_monitor_dic[host]['services'].keys():
                        self.global_monitor_dic[host]['services'][service.id] = [service, 0]  # 此处的0是为了以后计时用的。
                    else:
                        # 如果存在就更新数据。
                        self.global_monitor_dic[host]['services'][service.id][0] = service

                for trigger in trigger_list:
                    self.global_monitor_dic[host]['triggers'][trigger.id] = trigger
            print('self.global_monitor_dic:', self.global_monitor_dic)
            self.config_last_loading_time = time.time()
            return True





class ExpressionProcess(object):
    """
    通过触发器表达式，进行计算。(只是计算一条表达式的结果)
    """

    def __init__(self, main_ins, host_obj, expression_obj):
        self.host_obj = host_obj
        self.expression = expression_obj
        self.main_ins = main_ins

        # 生成redis中的key.用此key来
        self.service_redis_key = 'StatusData_%s_%s_latest' % (host_obj.id, expression_obj.service.name)
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

        # print('single_expression_calc_ret:',single_expression_calc_ret)

        # 如果单个结果不为空.
        if single_expression_calc_ret:
            res_dic = {
                'calc_res': single_expression_calc_ret[0],  # 判断是否报警的结果
                'calc_res_val:': single_expression_calc_ret[1],  # 用于判断结果的值（也就是计算出来的值）
                'expression_obj': self.expression,
                'service_item': single_expression_calc_ret[2]
            }

            # print('res_dic:', res_dic)
            return res_dic
        else:
            return False

    def load_data_from_redis(self):
        """
        从redis中取出符合要求的数据。
        :return:
        """
        time_in_sec = int(self.time_range) * 60  # 按分钟取
        # 多加一分钟的数据，并用此数除以服务的监控间隔（多久发一次数据），就可以得到大概要取多少条数据。
        approximate_data_points = int((time_in_sec + 60) / self.expression.service.interval)
        print('approximate_data_points:', approximate_data_points)

        # 从redis中取出的原始数据，从最后一个（-1)开始，往前取 approximate_data_points 个
        data_range_raw = self.main_ins.redis.lrange(self.service_redis_key, -approximate_data_points, -1)

        # 获得大概的数据列表。
        approximate_data_range = [json.loads(item) for item in data_range_raw]  # 列表推导式,返回的数据要进行返序列化处理。

        data_range = []  # 用于保存精确数据

        # 对大概数据进行分析，如果时间在范围内的就存入 data_range
        for point in approximate_data_range:
            val, saving_time = point
            if time.time() - saving_time < time_in_sec:  # 如果数据的时间在范围内.
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
                    for k, v in val['data'].items():
                        if k not in clean_data_dic.keys():
                            clean_data_dic[k] = []  # 对data中的每个字项生成一个列表。
                        clean_data_dic[k].append(v[self.expression.service_index.key])  # 在列表中存入监控指标的值。

            # 如果普通数据列表不为空
            if clean_data_list:
                # 将列表中的值转为float
                clean_data_list = [float(i) for i in clean_data_list]

                # 计算平平均值
                # avg_res = 0 if sum(clean_data_list) == 0 else sum(clean_data_list)/len(clean_data_list)
                avg_res = sum(clean_data_list) / len(clean_data_list)

                return [self.judge(avg_res), avg_res, None]

            if clean_data_dic:
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

        return calc_func(value, self.expression.threshold)  # 比较两个值并返回
