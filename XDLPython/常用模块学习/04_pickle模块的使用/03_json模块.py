#!/usr/bin/env python
# -*- coding utf-8 -*-
import json
'''json模块与pickle模块的用户，几乎一样，只是json在存入和取出文件时，要用字符模式，不能用字节模式'''

def f1():
    date = {
        1000: {'name': 'jim', 'age': 10, 'class': 1},
        2000: {'name': 'lily', 'age': 20, 'class': 2},
        3000: {'name': 'kimy', 'age': 30, 'class': 3}
    }

    with open('test01.json', 'w+') as f:
        json.dump(date, f)


def f2():
    with open('test01.json', 'r+') as f:
        '''用json.load返回的是对象，只是key值都变成了字符串，不是原来的数字了'''
        ret_dict = json.load(f)
        print(type(ret_dict))
        print(ret_dict['1000'])


def main():
    f2()


if __name__ == '__main__':
    main()
