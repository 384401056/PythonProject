#!/usr/bin/env python
# -*- coding utf-8 -*-


def fun1(a1,a2):
    return a1+a2


def main():
    # 此lambda表达式与fun1函数功能相同.
    fun2 = lambda a1,a2:a1+a2

    print(fun1(10,20))
    print(fun2(10,30)) # lambda表达式的调用也与函数相同




if __name__ == '__main__':
    main()