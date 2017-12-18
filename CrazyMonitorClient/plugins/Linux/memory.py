#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import locale


def monitor(first_invoke=1):
    """
    输出项说明：
    kbmemfree：这个值和free命令中的free值基本一致,所以它不包括buffer和cache的空间.
    kbmemused：这个值和free命令中的used值基本一致,所以它包括buffer和cache的空间.
    %memused：这个值是kbmemused和内存总量(不包括swap)的一个百分比.
    kbbuffers和kbcached：这两个值就是free命令中的buffer和cache.
    kbcommit：保证当前系统所需要的内存,即为了确保不溢出而需要的内存(RAM+swap).
    %commit：这个值是kbcommit与内存总量(包括swap)的一个百分比.
    :param first_invoke:
    :return:
    """
    value_dic = {'status': -1}
    """执行 sar 命令，获取linux系统的返回结果，放入字典并返回"""
    shell_command = 'sar -r 1 3|grep "^平均时间"'  # Linux系统命令
    shell_command = shell_command.encode(locale.getdefaultlocale()[1])  # 本地化中文字符
    cmd_ret = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE).stdout.read()
    result = str(cmd_ret, encoding='utf-8')

    if result != '':
        tup_ret = result.split()[1:]
        value_dic = {
            'kbmemfree': tup_ret[0],
            'kbmemused': tup_ret[1],
            '%memused': tup_ret[2],
            'kbbuffers': tup_ret[3],
            'kbcached': tup_ret[4],
            'kbcommit': tup_ret[5],
            '%commit': tup_ret[6],
            'kbactive': tup_ret[7],
            'kbinact': tup_ret[8],
            'kbdirty': tup_ret[9],
            'status': 0,
        }

    return value_dic
