#!/usr/bin/env python
# -*- coding utf-8 -*-


class Person:

    def __init__(self):
        print('__init__')


    def __call__(self, *args, **kwargs):
        print('__call__')



def main():
    obj = Person()

    obj() # 直接在对象后面加括号，就会去执行类中的__call__方法.


if __name__ == '__main__':
    main()