#!/usr/bin/env python
# -*- coding utf-8 -*-
import re


def fun_sub():
    '''用正则匹配要替换的字符串'''
    my_str = '234abcde456ertew789ioudehjk'
    ret = re.sub('\d+', 'O', my_str) # 使用字母O,来替换字符串中的数字
    print(ret)


def fun_subn():
    '''用正则匹配要替换的字符串'''
    my_str = '234abcde456ertew789ioudehjk'
    ret, num = re.subn('\d+', 'O', my_str) # 使用字母O,来替换字符串中的数字,返回一个元组。
    print(ret)
    print(num)

def main():
    fun_subn()


if __name__ == '__main__':
    main()
