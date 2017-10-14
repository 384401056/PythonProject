#!/usr/bin/env python
# -*- coding utf-8 -*-
import sys
import time
'''跟解释器相关的都在sys模块中。'''


def f1():
    print(sys.argv)  # 返回执行脚本时，输入的参数
    print(sys.path)  # 返回python的路径
    print(sys.platform) # 返回操作系统平台名称
    print('python version: ', sys.version) # 显示python的版本



def f2():
    choice = input("要退出吗？").strip()
    if choice == 'y' or choice == 'Y':
        sys.exit("Goodbye!") # 退出程序, 与exit()功能相同


def f3():
    '''获取用户输入'''
    cmd = sys.stdin.readline()
    print(cmd)

def main():
    f3()




if __name__ == '__main__':
    main()