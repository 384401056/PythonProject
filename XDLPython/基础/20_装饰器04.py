#!/usr/bin/env python
# -*- coding utf-8 -*-
'''多个装饰器装饰同一个函数'''

def outer(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret

    return inner()


def f1():
    print('f1')


def main():
    pass


if __name__ == '__main__':
    main()
