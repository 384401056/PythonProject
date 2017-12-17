#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import locale

def monitor(first_invoke=1):
    value_dic = {'status': -1}
    """执行 sar 命令，获取linux系统的返回结果，放入字典并返回"""
    shell_command = 'sar 1 3|grep "^平均时间"'  # Linux系统命令
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
    return value_dic