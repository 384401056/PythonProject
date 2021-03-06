#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import locale
import logging
from conf import settings

log = logging.getLogger('crazyclient')

def monitor(first_invoke=1):
    """
    IFACE：LAN接口
    rxpck/s：每秒钟接收的数据包
    txpck/s：每秒钟发送的数据包
    rxbyt/s：每秒钟接收的字节数
    txbyt/s：每秒钟发送的字节数
    rxcmp/s：每秒钟接收的压缩数据包
    txcmp/s：每秒钟发送的压缩数据包
    rxmcst/s：每秒钟接收的多播数据包

    平均时间:     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s   %ifutil
    平均时间:        lo     24.58     24.58      4.29      4.29      0.00      0.00      0.00      0.00
    平均时间:      eth0    209.63    207.31    184.65     27.28      0.00      0.00      0.00      0.00

    :param first_invoke:
    :return:
    """
    try:
        value_dic = {'status': -1}

        cmd_Average = '"' + settings.cmd_lang[settings.languarge] + '"' #根据系统的语言设置返回的Average字符

        """执行 sar 命令，获取linux系统的返回结果，放入字典并返回"""
        shell_command = 'sar -n DEV 1 3|grep ' + cmd_Average  # Linux系统命令
        # shell_command = shell_command.encode(locale.getdefaultlocale()[1])  # 本地化中文字符
        cmd_ret = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE).stdout.read()
        result = str(cmd_ret, encoding='utf-8')

        if result != '':
            value_dic = {
                'status': 0,
                'data': resolve_data_type(result),
            }
    except Exception as ex:
        log.error('%s' % ex)
        # print(ex)
    finally:
        return value_dic


def resolve_data_type(result):
    """将多个结果集的字符串解析为data{}"""
    tup = result.split("平均时间:")[2:]
    ret_dict = {}
    for s in tup:
        temp = s.split()
        ret_dict[temp[0]] = {
            'rxpck': temp[1],
            'txpck': temp[2],
            'rxbyt': temp[3],
            'txbyt': temp[4],
            'rxcmp': temp[5],
            'txcmp': temp[6],
            'rxmcst': temp[7],
            'ifutil': temp[8],
        }
    return ret_dict

