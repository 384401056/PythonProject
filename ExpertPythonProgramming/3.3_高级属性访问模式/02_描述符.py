#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.initval = initval
        self.name = name

    def __get__(self, instance, owner):
        print("get")
        return self.name

    def __set__(self, instance, value):
        print('set')
        self.name = value

class MyClass(object):
    x = RevealAccess(10, "KKK")
    y = 20

def main():
    m = MyClass()
    print(m.x)
    m.x = 20

if __name__ == '__main__':
    main()