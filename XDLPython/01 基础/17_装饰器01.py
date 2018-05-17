#!/usr/bin/env python
# -*- coding utf-8 -*-

def outer(func):
    print('outer exec...')
    print(func())
    return 456

'''
定义装饰器,当python解释器执行到装饰器时，会完成二件事
1. 执行outer函数，并将f1做为参数传给outer。
2. 将outer函数的返回值，赋值给f1.
'''
@outer
def f1():
    print('f1 exec...')
    return 123



def main():
    print(f1) # 执行带有装饰器的函数。
    # a = f1()
    # print(a)


if __name__ == '__main__':
    main()