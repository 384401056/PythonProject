#!/usr/bin/env python
# -*- coding utf-8 -*-

import lib.account as ac


def f1():
    ''' 动态调用方法 '''
    url = input("输入地址:")

    inp = url.split('/')[-1]  # 取出最后一个字符

    if hasattr(ac, inp):
        attr = getattr(ac, inp)
        print(attr())
    else:
        print('404')


def f2():
    ''' 动态导入模块，并调用方法 '''
    url = input("输入地址:")
    mod_str, func_str = url.split('/')

    mod = __import__('lib.' + mod_str, fromlist=True)

    if hasattr(mod, func_str):
        func = getattr(mod, func_str)
        ret = func()
        print(ret)


def main():
    f2()


if __name__ == '__main__':
    main()
