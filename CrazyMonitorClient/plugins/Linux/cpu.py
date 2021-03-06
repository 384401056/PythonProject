#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import locale
from conf import settings
import logging

log = logging.getLogger('crazyclient')

def monitor(first_invoke=1):

    try:
        value_dic = {'status': -1}

        cmd_Average = '"' + settings.cmd_lang[settings.languarge] + '"' #根据系统的语言设置返回的Average字符

        """执行 sar 命令，获取linux系统的返回结果，放入字典并返回"""
        shell_command = 'sar 1 3|grep ' + cmd_Average  #

        shell_command = shell_command.encode(locale.getdefaultlocale()[1])  # 本地化中文字符
        cmd_ret = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE).stdout.read()
        result = str(cmd_ret, encoding='utf-8')
        # 如果没出错
        if result != '':
            user, nice, system, iowait, steal, idle = result.split()[2:]  # 从字符串的第二段开始截取
            value_dic = {
                'user': user,
                'nice': nice,
                'system': system,
                'iowait': iowait,
                'steal': steal,
                'idle': idle,
                'status': 0,
            }
            '''
            %user：显示在用户级别(application)运行使用 CPU 总时间的百分比。
            %nice：显示在用户级别，用于nice操作，所占用 CPU总时间的百分比。
            %system：在核心级别(kernel)运行所使用 CPU总时间的百分比。
            %iowait：显示用于等待I/O操作占用 CPU总时间的百分比。
            %steal：管理程序(hypervisor)为另一个虚拟进程提供服务而等待虚拟 CPU 的百分比。
            %idle：显示 CPU空闲时间占用 CPU总时间的百分比。

            1.若 %iowait的值过高，表示硬盘存在I/O瓶颈
            2.若 %idle的值高但系统响应慢时，有可能是 CPU等待分配内存，此时应加大内存容量
            3.若 %idle的值持续低于1，则系统的 CPU处理能力相对较低，表明系统中最需要解决的资源是 CPU。
            '''
    except Exception as ex:
        log.error('%s' % ex)
        # print(ex)
    finally:
        return value_dic
