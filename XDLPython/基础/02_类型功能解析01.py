#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    temp = 'alex'
    print(type(temp)) # 查询变量类型
    print(dir(type(temp))) # 查看str类的所有方法
    print(help(type(temp))) # 类的帮助文件



def main2():
    '''整数'''
    a = int('1000')
    len = a.bit_length() # 返回整数的二进制最小可表示的位数.
    print(a)
    print(len)
    print((10).bit_length())


def main3():
    '''字符串'''
    str


if __name__ == '__main__':
    main2()