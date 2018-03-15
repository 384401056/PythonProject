#!/usr/bin/env python
# -*- coding utf-8 -*-

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('name: %s' % self.name)
        print('age: %d' % self.age)

    # 类方法
    @classmethod
    def clsfunc(cls):
        print("I'm a class function!!!!")
        print(cls) # cls指调用此方法的类


def main():
    # print(Person.__dict__)
    Person.clsfunc() # 调用类方法


    obj1 = Person('jim', 20)
    obj1.clsfunc() # 通过对象来调用类方法


if __name__ == '__main__':
    main()