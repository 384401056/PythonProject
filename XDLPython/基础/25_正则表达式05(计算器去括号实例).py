#!/usr/bin/env python
# -*- coding utf-8 -*-

import re
'''计算器去括号实例'''


def count(exp):
    '''计算表达式的值并返回，如果无法完成计算则抛出异常'''
    scope = {}
    try:
        exec('a=' + exp, scope)
        return scope['a']
    except Exception as erro:
        # print(erro)
        raise  # 如果无法计算，则抛出异常。


def f1(expression):
    '''计算器去括号实例'''
    ret = re.split(r'\(([^()]+)\)', expression)  # 以 ( 开头,以 ) 结尾，并且中间不再包含()的字符串来进行分割。并且保留分割的字符.
    # print(ret)
    for (index, exp) in enumerate(ret):
        if '(' not in exp and ')' not in exp:
            try:
                a = str(count(exp))
                ret[index] = a # 用计算后的结果，替换原来的公式
            except Exception as erro:
                pass

    # 如果列表中只有一个元素，就印出最后结果
    if len(ret) > 1:
        expression = ''
        for exp in ret:
            expression += exp  # 生成新的表达式
        # print(expression)
        f1(expression)  # 递归调用
    else:
        print(ret[0])


def main():
    f1("(50-(3+2)*(4+7)+25)/2")


if __name__ == '__main__':
    main()
