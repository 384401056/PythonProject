#!/usr/bin/env python
# -*- coding utf-8 -*-


def xrange(n):
    '''自定义xrange的实现'''
    start = 0
    while True:
        if start > n:
            return
        yield start
        start += 1


def main():

    obj = xrange(10)

    # 只有在调用__next__()时才会生成新的数据，而不是一次生成所有数据.
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())


if __name__ == '__main__':
    main()
