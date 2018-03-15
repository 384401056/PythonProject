#!/usr/bin/env python
# -*- coding utf-8 -*-

class Person:
    __mylist = list()

    def __init__(self):
        pass

    def __getitem__(self, item):
        print(item, type(item), '__getitem__')

    def __setitem__(self, key, value):
        print(key, value, '__setitem__')

    def __delitem__(self, key):
        print(key, '__delitem__')


def main():
    person = Person()

    person[1:2]  # 用list的形式访问了对象,此时会执行__getitem__方法, 参数item会被封装成一个slice对象

    person[0] = 'aaa'  # 用list的形式访问了对象,此时会执行__setitem__方法。其中参数key为0， value为aaa

    del (person[0])  # 用list的形式访问了对象,此时会执行__delitem__方法，其中参数key为0


if __name__ == '__main__':
    main()
