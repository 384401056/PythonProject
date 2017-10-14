#!/usr/bin/env python
# -*- coding utf-8 -*-
import re


def f1():
    '''字符串的分割'''

    # 不分组
    my_str = 'hello way my home tail miss my zoom iphone'
    ret = re.split(' ', my_str, maxsplit=1)  # maxsplit 最大分割次数.
    ret = re.split(' ', my_str)
    ret = re.split('t\w+', my_str)  # 以t开头的字符串进行分割.此时正则表达式本身，不会存在于分完的组中。

    # 　分组后 正则表达式本身，会存在于分完的组中
    ret = re.split('(t\w+)', my_str)
    ret = re.split('t(\w+)', my_str)
    print(ret)


def main():
    f1()


if __name__ == '__main__':
    main()
