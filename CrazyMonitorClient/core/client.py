#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
import requests
import threading
import locale
from conf import settings
from plugins import plugin_api


class ClientHandler(object):

    def __init__(self):
        self.monitor_services = {}

    def forever_run(self):
        """
        启动client程序,主线程就是在维护一个循环，每秒种判断一次是否到了采集间隔时间。
        如果到了，就采集数据。
        1. 先去服务端获取配置信息。
        2. 解析主机的配置信息。
        3.
        :return:
        """
        exit_flag = False  # 循环停止位.
        config_last_update_time = 0  # 最后一次更新配置的时间.
        while not exit_flag:
            # 如果当前时间-最后一次更新的时间(ConfigUpdateInterval).就去服务器端获取配置数据。
            if time.time() - config_last_update_time > settings.configs['ConfigUpdateInterval']:
                self.load_last_configs()
                config_last_update_time = time.time()

            # 解析主机的配置信息
            for serv_name, val in self.monitor_services['services'].items():
                # print('serv_name:', serv_name)
                # print('val:', val)

                if len(val) == 2:
                    # 对json字符串本身进行修改，在服务名对应的值中，加入一个0，用于记录上次采集数据的时间
                    # 以随于对时间间隔进行判断。
                    self.monitor_services['services'][serv_name].append(0)

                monitor_interval = val[1]  # 执行间隔.
                last_invoke_time = val[2]  # 上次执行时间.

                # 如果符合时间间隔要求,重置采集时间。并开启子线程执行插件。
                if time.time() - last_invoke_time > monitor_interval:
                    self.monitor_services['services'][serv_name][2] = time.time()  # 重置时间。
                    t = threading.Thread(target=self.invoke_plugin, args=(serv_name, val))
                    t.start()
                    print('Going to monitor [%s]' % serv_name)
                else:
                    invoke_time = round(monitor_interval - (time.time() - last_invoke_time))  # 采集时间倒计时.round四舍五入
                    print('Going to monitor [%s] in [%s]' % (serv_name, invoke_time,))

            # print('configs:', self.monitor_services)  # 打印出获取到的配置信息。
            time.sleep(1)  # 1秒循环一次。
            # print(time.time())

    def invoke_plugin(self, serv_name, val):
        """运行插件"""
        plugin_name = val[0]

        # 通过反射来执行插件函数
        if hasattr(plugin_api, plugin_name):
            func = getattr(plugin_api, plugin_name)
            plugin_ret = func()
            print('plugin_ret', plugin_ret)
            report_data = {
                'client_id': settings.configs['HostID'],
                'server_name': serv_name,
                'data': json.dumps(plugin_ret)
            }

            # 上报数据
            report_type = settings.configs['urls']['server_report'][1]
            # 拼接URL，带上客户端的id.
            report_url = settings.configs['urls']['server_report'][0]
            ret = self.url_request(report_type, report_url, data=report_data)
            print('from server:', ret)


    def load_last_configs(self):
        """
        从服务器加载配置
        :return:
        """
        request_type = settings.configs['urls']['get_configs'][1]
        # 拼接URL，带上客户端的id.
        url = '%s/%s' % (settings.configs['urls']['get_configs'][0], settings.configs['HostID'])
        # 从服务器端获取配置，转为json格式。再更新monitor_services字典。
        ret = self.url_request(request_type, url)
        latest_configs = json.loads(ret)
        self.monitor_services.update(latest_configs)
        print('configs:', self.monitor_services)  # 打印出获取到的配置信息。

    def url_request(self, method, url, **extra_data):
        """
        通过url接口，向服务器端请求数据或者发送数据。
        :param request_type:
        :param url:
        :param kwargs:
        :return:
        """
        abs_url = 'http://%s:%s/%s' % (
            settings.configs['Server'],
            settings.configs['ServerPort'],
            url,
        )

        # print('abs_url', abs_url)

        if method.upper() == 'GET':
            try:
                # ret = requests.get('http://127.0.0.1:8080/coap',params=transaction.request.payload)
                # ret = requests.post('http://127.0.0.1:8080/coap', data={'payload': transaction.request.payload})
                response = requests.get(abs_url, timeout=settings.configs['RequestTimeout'])
                response_data = response.text
                return response_data
            except Exception as ex:
                print(ex)
                exit()
        elif method.upper() == 'POST':
            try:
                response = requests.post(abs_url, data=extra_data['data'], timeout=settings.configs['RequestTimeout'])
                response_data = response.text
                return response_data
            except Exception as ex:
                print(ex)
                exit()

def main():
    pass


if __name__ == '__main__':
    main()
