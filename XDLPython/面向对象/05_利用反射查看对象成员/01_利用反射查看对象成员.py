#!/usr/bin/env python
# -*- coding utf-8 -*-

class Person:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name, ' show方法被调用')


def main():

    person = Person("Jimson")

    print(Person.__dict__) # 查看类的成员。
    # 利用反射通过类来调用方法
    if hasattr(Person, 'show'):
        attr = getattr(Person, 'show')
        attr(person)


    print(person.__dict__)  # 查看对象成员
    # 利用反射通过对象来访问字段
    if hasattr(person, 'name'):
        print(getattr(person, 'name'))

    # 利用反射通过对象来访问类中的方法
    if hasattr(person, 'show'):
        attr = getattr(person, 'show')
        attr()



if __name__ == '__main__':
    main()