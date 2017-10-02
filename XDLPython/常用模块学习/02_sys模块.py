#!/usr/bin/env python
# -*- coding utf-8 -*-
import sys
import time

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
    '''以下代码要在python命令行下才有效果'''
    for i in range(10):
        sys.stdout.write("#") # 在系统屏幕输出
        time.sleep(1)

def f4():
    '''获取用户输入'''
    cmd = sys.stdin.readline()
    print(cmd)

def main():
    f4()




if __name__ == '__main__':
    main()