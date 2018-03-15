#!/usr/bin/env python
# -*- coding utf-8 -*-
import re


def f1():
    '''正则表达式：{} 代表字符的重复次数'''
    print(re.findall('alex{3}', 'alexxxfdsafalexxxxx'))  # 查找x有3个的
    print(re.findall('alex{3,5}', 'alexxxfdsafalexxxxxx'))  # 查找x有3-5个, 3和5之前不能有空格。


def f2():
    '''正则表达式：[] 代表一个字符范围,匹配指定范围内的任意字符。'''
    print(re.findall('a[bcd]e', 'alexabealexxacex')) # 其中b,c,d 之间是或者的关系.
    print(re.findall('a[.]e', 'abe323klkadeklja.e'))  # 在这个字符范围中的其它原字符都是无效的。
    print(re.findall('a[a-z]e', 'abeaceadeaeeafeazeayeaxe'))  # - 在字符范围中代表一个区间
    print(re.findall('a[A-Z]e', 'aBeaceadeaEeafeazeaYeaxe'))
    print(re.findall('a[0-9]e', 'a0eacea8eaEeafea4eaYea9e'))
    print(re.findall('a[^0-9]e', 'a0eacea8eaEeafea4eaYea9e')) # ^ 代表除了指定字符外的字符.


def f3():
    '''正则表达式：() 标记一个子表达式的开始和结束位置'''
    pass


def f4():
    '''正则表达式: '\' 当其后有原字符时，去除原字符的特殊功能。当其后不是原字符时，赋予其特殊功能 '''
    print(re.findall('\d','fds  f233dfewe dfdsazE@WECDS#%^#1232')) # 相当于[0-9]
    print(re.findall('\D','fds  f233dfewe dfdsazE@WECDS#%^#1232')) # 相当于[^0-9]
    print(re.findall('\s','fds  f233dfewe dfdsazE@WECDS#%^#1232')) # 相当于[\t\n\r\f\v] 匹配任意空白字符
    print(re.findall('\S','fds  f233dfewe dfdsazE@WECDS#%^#1232')) # 相当于[^ \t\n\r\f\v] 匹配任意非空白字符
    print(re.findall('\w', 'fds  f23$#@#$^$%&%&*fewe dfdsazE@WECDS#%^#1232'))  # 相当于[A-Za-z0-9]
    print(re.findall('\W', 'fds  f23$#@#$^$%&%&*fewe dfdsazE@WECDS#%^#1232'))  # 相当于[^ A-Za-z0-9]

def f5():
    '''正则表达式：| 代表或的关系。正则表达式:?: 代表去除()中优先捕获的功能'''
    print(re.findall('www.(baidu|163).com','www.163.comfdsafdsafdsawww.baidu.com')) # 此时findall会优先捕获和返回()中匹配成功的内容
    print(re.findall('www.(?:baidu|163).com','www.163.comfdsafdsafdsawww.baidu.com')) # 此时findall会去除优先捕获的功能

def main():
    f5()


if __name__ == '__main__':
    main()
