#!/usr/bin/env python
# -*- coding utf-8 -*-

def fun1(a1, a2):
    return a1 + a2


def fun2(arg):
    print(arg)


def fun3(arg):
    print(arg())


def myfilter(fun, seq):
    '''自定义过滤器函数'''
    result = []
    for i in seq:
        ret = fun(i)
        if ret:
            result.append(i)
    return result;


def filter_fun(i):
    return i > 50


def main():
    '''将函数做为别一个函数的参数。'''
    fun2(fun1(10, 20))

    a = lambda:1000 # 定义一个lambda函数
    print(a())

    fun3(a)

    '''自定义过滤器'''
    ret = myfilter(filter_fun, [11, 22, 33, 44, 55, 66, 77, 88]) # 过滤掉小于50的数字
    print(ret)


if __name__ == '__main__':
    main()
