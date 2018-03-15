#!/usr/bin/env python
# -*- coding utf-8 -*-

import subprocess

'''用于执行操作系统命令, 及管理子进程'''


def f1():
    '''执行简单的系统命令'''
    # 执行系统命令，返回0
    # ret = subprocess.call('ipconfig')
    # print(ret)

    # 执行系统命令，返回执行结果(bytes类型)
    ret = subprocess.check_output('ipconfig')

    # print(str(ret, encoding='gbk')) # 直接输出gbk字符串

    ret_byte = ret.decode('gbk').encode('utf-8')  # 将返字符从gbk转成utf-8字节
    ret_utf8 = str(ret_byte, encoding='utf-8')  # 将字节转为utf-8字符串
    print(ret_utf8)


def f2():
    '''执行复杂的系统命令'''



def main():
    f1()




if __name__ == '__main__':
    main()
