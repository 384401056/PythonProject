#!/usr/bin/env python
# -*- coding utf-8 -*-

class Person:

    def __init__(self):
        pass

    def __iter__(self):
        yield 10
        yield 20
        yield 30
        yield 40



def main():
    p = Person()

    # 当对一个对象进行迭代操作时，会去执行类中的__iter__方法。
    # 并且此方法必须要为生成器(yield),迭代才能成功。
    for i in p:
        print(i)


if __name__ == '__main__':
    main()