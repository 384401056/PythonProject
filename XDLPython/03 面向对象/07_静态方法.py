#!/usr/bin/env python
# -*- coding utf-8 -*-

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('name: %s' % self.name)
        print('age: %d' % self.age)

    # 类中的静态方法
    @staticmethod
    def display():
        print("I'm a static function!!!!")


def main():
    # print(Person.__dict__)
    Person.display() # 调用静态方法


    obj1 = Person('jim', 20)
    obj1.display() # 通过对象来调用静态方法


if __name__ == '__main__':
    main()