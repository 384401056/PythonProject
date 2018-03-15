#!/usr/bin/env python
# -*- coding utf-8 -*-
'''带有多个参数的装饰器定义方法'''

def outer(func):
    def inner(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')

    return inner


@outer  # 对带参数的函数使用装器
def f1(a, b):
    print(a + b)

@outer
def f2(a):
    print(a)


def main():
    f1(10, 30)
    f2(200)


if __name__ == '__main__':
    main()
