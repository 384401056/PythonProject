#!/usr/bin/env python
# -*- coding utf-8 -*-


class Animals:
    def eat(self):
        print('%s 在吃东西' % self.name)

    def run(self):
        print('%s 在跑步' % self.name)


class Life:
    def blood(self):
        print('%s 在流血' % self.name)

    def run(self):
        print('%s 在奔跑...' % self.name)

# Dog类继承自Animals类和Life (多继承)
class Dog(Animals, Life):

    def __init__(self, name):
        self.name = name

    def barking(self):
        print('%s 在叫' % self.name)


def main():
    dog = Dog('大黄')
    dog.barking() # 调用自己类的方法.
    dog.eat() # 调用父类Animals的方法
    dog.blood() # 调用父类Life的方法

    dog.run() # 如果多继承的父类中有相同的方法，则先继承的优先（左边优先）


if __name__ == '__main__':
    main()