#!/usr/bin/env python
# -*- coding: utf-8 -*-


def singleton(cls):
    '''
    装饰器
    :param cls: 被装饰的类
    :return:
    '''
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton
class MyClass():
    def foo(self):
        print("foo")

# MyClass此时type为function, 所以不能作为父类。
# class MyChildClass(MyClass):
#     pass

def main():

    c1 = MyClass()
    c2 = MyClass()

    print(c1)
    print(c2)

    print(c1 is c2)

if __name__ == '__main__':
    main()