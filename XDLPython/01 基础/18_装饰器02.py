#!/usr/bin/env python
# -*- coding utf-8 -*-

def outer(func):
    def inner():
        print('start')
        print('start')
        r = func() # 执行f1
        print('end')
        print('end')
        return r
    return inner

'''
定义装饰器,当python解释器执行到装饰器时，会完成二件事
1. 执行outer函数，并将f1做为参数传给outer。
2. 将outer函数的返回值，赋值给f1.
装饰器在f1函数之前和之后执行了某些代码，并且不影响f1原函数的执行和原函数的返回值
'''
@outer # 注释此句代码会看得更清楚
def f1():
    print('f1')
    return "xxx"



def main():
    a= f1()
    print(a)

if __name__ == '__main__':
    main()