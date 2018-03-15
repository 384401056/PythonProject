#!/usr/bin/env python
# -*- coding utf-8 -*-

'''
在python中的成员修饰符分为：公有、和私有。
在类中被 __ 修饰的私有字段或者方法，只有在自己类中可以访问，从外部是无法访问的，同时自己的子类也无法访问

但是在python中也有一种特殊的方法可以访问到私有的字段和方法，只是不推荐这样去做。
格式： 对象._类名(父类)__私有字段名
      对象._类名(父类)__私有方法名()

'''



class Person:
    id = '123456788'
    __id = '123456788'  # 类私用的字段

    def __init__(self, name, age):
        self.__name = name  # 对象的私有字段
        self.__age = age

    def fetch(self):
        print(Person.__id)
        print(self.__name)
        print(self.__age)

    def __func(self):
        print('Person kiss')


class Foo(Person):

    def kiss(self):
        print(self.__name)
        print(self.__age)


def main():
    print(Person.id)
    # print(Person.__id) # 无法从类的外部访问类内部的私用字段。

    obj = Person('Jimson', 20)
    obj.fetch()  # 通过方法可以访问类内部的字段。

    # print(obj.__name) # 无法从类的外部访问对象的私用字段
    # print(obj.__age)

    # 一种特殊的访问私有字段和方法的做法是：但是极度不推荐使用。
    # print(obj._Person__name)
    # print(obj._Person__age)
    # obj._Person__func()


    obj2 = Foo('KKK', 2000) # 调有父类的初始化方法.
    obj2.fetch()  # 调用父类的方法可以访问父类的么有字段
    # obj2.kiss() # 无法在子类的方法中访问父类的私有字段
    # obj2.__func() # 无法在子类中访问父类的私有方法




if __name__ == '__main__':
    main()
