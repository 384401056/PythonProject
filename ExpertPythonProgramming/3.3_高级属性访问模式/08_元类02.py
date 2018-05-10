#!/usr/bin/env python
# -*- coding: utf-8 -*-


def func(self, value):
    self.append(value)


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        '''
        __new__()方法接收到的参数依次是：
        1. 当前准备创建的类的对象；
        2. 类的名字；
        3. 类继承的父类集合；
        4. 类的方法集合。
        '''
        attrs['add'] = func # 为类增加一个add方法.
        return type.__new__(cls, name, bases, attrs)
        # attrs['add'] = lambda self, value: self.append(value) # 或者定义一个lambda
        # return super().__new__(cls, name, bases, attrs) # 效果同上

"""
当我们写下__metaclass__ = ListMetaclass语句时，魔术就生效了，
它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
"""
class MyList(list, metaclass=ListMetaclass): # 它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建,这是python3.0的元类写法与2.x有很大区别。
    pass


def main():
    l = MyList()
    l.add(2)
    print(l)


if __name__ == '__main__':
    main()