#!/usr/bin/env python
# -*- coding utf-8 -*-

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def show(self):
        print('name: %s' % self.name)
        print('age: %d' % self.age)

    # 特性（属性）：将方法伪造成一种字段
    @property
    def getName(self):
        return self.name

    @property
    def getAge(self):
        return self.age

    @getName.setter # setter装饰器表明，这是为getName特性设置值的方法。
    def setName(self, value):
        self.name = value
        print(value)

    @getName.setter # setter装饰器表明，这是为getAge特性设置值的方法。
    def setAge(self, value):
        self.age = value
        print(value)


def main():
    obj = Person('lily', 29)

    # 对特性的访问
    print(obj.getName)
    print(obj.getAge)

    # 对特性值的设置
    obj.setName = 'Jimasony'
    obj.setAge = 200

    print(obj.getName)
    print(obj.getAge)


if __name__ == '__main__':
    main()
