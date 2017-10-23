#!/usr/bin/env python
# -*- coding utf-8 -*-

class Person:
    ''' 通过类的静态方法 getInstance 创建的对象，就是单例的。 '''
    __instance = None

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @staticmethod
    def getInstance(name, age):
        ''' 实现创建单例对象 '''

        # 如果已经创建过一个对象，则返回.(实现单例）
        if Person.__instance is None:
            Person.__instance = Person(name, age)
        return Person.__instance



def main():

    # obj1 和 obj2 的内存地址是同一个，说明他们是同一个对象.
    obj1 = Person.getInstance('kkk',20)
    print(obj1)
    obj2 = Person.getInstance('bbb', 30)
    print(obj2)

    # obj3没有通过类的静态方法创建对象，所以是一个新的对象。
    obj3 = Person('aaa', 50)
    print(obj3)


if __name__ == '__main__':
    main()