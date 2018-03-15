#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conf import settings
import sys, os

result = """
平均时间:     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s   %ifutil
平均时间:        lo     24.58     24.58      4.29      4.29      0.00      0.00      0.00      0.00
平均时间:      eth0    1    1    1     27.28      0.00      0.00      0.00      0.00
平均时间:      eth1    2    2    184.65     27.28      0.00      0.00      0.00      0.00
平均时间:      eth2    3    3    184.65     27.28      0.00      0.00      0.00      0.00
""".strip()

def resolve_data_type(result):
    """将多个结果集的字符串解析为data{}"""
    tup = result.split("平均时间:")[2:]
    ret_dict = {}
    for s in tup:
        temp = s.split()
        ret_dict[temp[0]] = {
            'rxpck/s':temp[1],
            'txpck/s':temp[2],
            'rxkB/s/s':temp[3],
            'txkB/s':temp[4],
            'rxcmp/s':temp[5],
            'txcmp/s':temp[6],
            'rxmcst/s':temp[7],
            ' %ifutil':temp[8],
        }

    return ret_dict


def help_msg():
    valid_command = '''
    command is not right.
    params[1]:
    start      start monitor client.
    stop       stop monitor client.
    params[2]:
    cn         Chinese
    en         English
    '''
    exit(valid_command) # 交互式shell


def main(argv):
    # value_dic = {
    #     'status': 0,
    #     'data': resolve_data_type(result),
    # }
    #
    # print(value_dic)

    # 如参数长度小于2
    if len(argv) < 3:
        # print(help_msg())
        exit(help_msg())

    if (argv[2] in settings.cmd_lang):
        # 设置语言
        settings.languarge = argv[2]

        cmd_Average = '"' + settings.cmd_lang[settings.languarge] + '"'
        shell_command = 'sar 1 3|grep ' + cmd_Average  # Linux系统命令

        if (argv[1] in ['start', 'stop']):
            print(shell_command)
            print('run cmd....')
        else:
            exit(help_msg())
    else:
        exit(help_msg())
    # cmd_str = '"'+settings.cmd_lang[settings.languarge]+'"'
    # print(cmd_str)


if __name__ == '__main__':
    main(sys.argv)