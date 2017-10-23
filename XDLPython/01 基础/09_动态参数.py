#!/usr/bin/env python
# -*- coding utf-8 -*-


def fun1(*a):
    ''''动态参数,参数类型默认为元组'''
    print(a, type(a))


def fun2(**a):
    '''动态参数，参数类型默认为字典,有两个星号的动态参数只能传入键值对'''
    print(a, type(a))

def fun3(*a1, **a2):
    '''一个星的参数一定要在二个星参数的前面。'''
    print(a1, type(a1))
    print(a2, type(a2))


def main():
    fun1(100,['aa','bb'])
    fun1(*(100,200,300,400)) # 当传入参数就是元组前面加*
    fun2(k1=200,k2=300)
    fun2(**{'k1':200,'k2':300}) # 当传入参数就是字典前面加**
    fun3(100,200,k1=323,k2=2343,k4=3232)


if __name__ == '__main__':
    main()