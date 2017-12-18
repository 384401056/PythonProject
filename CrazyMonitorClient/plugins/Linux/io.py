#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import locale


def monitor(first_invoke=1):
    """
    I/O和传送速率监控
    :param first_invoke:
    :return:
    tps：每秒钟物理设备的 I/O 传输总量
    rtps：每秒钟从物理设备读入的数据总量
    wtps：每秒钟向物理设备写入的数据总量
    bread/s：每秒钟从物理设备读入的数据量，单位为 块/s
    bwrtn/s：每秒钟向物理设备写入的数据量，单位为 块/s
    """
    value_dic = {'status': -1}
    """执行 sar 命令，获取linux系统的返回结果，放入字典并返回"""
    shell_command = 'sar -b 1 5|grep "^平均时间"'  # Linux系统命令
    shell_command = shell_command.encode(locale.getdefaultlocale()[1])  # 本地化中文字符
    cmd_ret = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE).stdout.read()
    result = str(cmd_ret, encoding='utf-8')

    if result != '':
        tup_ret = result.split()[1:]
        value_dic = {
            'tps': tup_ret[0],
            'rtps': tup_ret[1],
            'wtps': tup_ret[2],
            'bread/s': tup_ret[3],
            'bwrtn/s': tup_ret[4],
            'status': 0,
        }

    return value_dic

