#!/usr/bin/env python
# -*- coding utf-8 -*-


class Person:

    def __init__(self):
        print('__init__')


    def __str__(self):
        return '这是一个Person对象'



def main():
    obj = Person()
    print(obj) # 直接输出对象，就会去执行类中的__str__方法.


if __name__ == '__main__':
    main()