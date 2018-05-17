#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用metaclass（元类）实现单例模式：
元类可以控制类的创建过程，它主要做三件事：
　　- 拦截类的创建
　　- 修改类的定义
　　- 返回修改后的类
"""
class Singleton(type):

    def __init__(self, *args, **kwargs):
        self._instance = None
        super(Singleton,self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super(Singleton,self).__call__(*args, **kwargs)
        return self._instance


class MyClass(object, metaclass=Singleton):
    """
    实现了单例的类
    """
    pass

class MyChildClass(MyClass):
    """子类"""
    pass


def main():
    # 使用元类的方式，不会出现01__new__代码中，由于创建对象先后顺序不同，出现不可预知的情况。
    # 子类的对象永远和父类不是一个对象。也就安全子类化。
    c2 = MyClass()
    c1 = MyChildClass()
    c3 = MyClass()

    print(c1)
    print(c2)
    print(c3)

    print(c1 is c2 is c3)

if __name__ == '__main__':
    main()