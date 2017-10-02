#!/usr/bin/env python
# -*- coding utf-8 -*-


import getpass  # 注，此模块在pycharm中无法使用。要在命令行执行才有效果

def main():
    username = input("username:")
    password = getpass.getpass("password:")  # 让用户输入密码（输入时不显示字符）此模块在pycharm中无法使用。要在命令行执行才有效果
    print(username, password)


if __name__ == '__main__':
    main()
# 当被作为库使用时，也直接执行main()函数
else:
    main()