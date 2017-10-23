#!/usr/bin/env python
# -*- coding utf-8 -*-

class Foo:

    # 通过构造方法传入要封装的值。并将它赋值给self中的属性.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showFoo(self):
        print('name : %s' % self.name)
        print('age : %d' % self.age)


def main():
    foo1 = Foo('Jim', 20)
    foo2 = Foo('lily', 30)

    foo1.showFoo()
    print('----------------------------')
    foo2.showFoo()


if __name__ == '__main__':
    main()
