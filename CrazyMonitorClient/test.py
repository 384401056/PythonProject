#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

def main():
    value_dic = {
        'status': 0,
        'data': resolve_data_type(result),
    }

    print(value_dic)

if __name__ == '__main__':
    main()