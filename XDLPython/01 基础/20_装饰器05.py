#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
参数化装饰器,可接收参数的装饰器。
"""


def repeat(number=3):
    """
    这样定义的装饰器可以接收参数
    :param number: 被装饰函数执行的次数
    :return:
    """

    def actual_decoratio(func):
        def wrapper(*args, **kwargs):
            result = None;
            for i in range(number):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return actual_decoratio


@repeat(2)
def foo(a, b):
    print("foo", a+b)


def main():
    foo(1, 2)


if __name__ == '__main__':
    main()
