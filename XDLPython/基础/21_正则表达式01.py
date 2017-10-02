#!/usr/bin/env python
# -*- coding utf-8 -*-
import re


def f1():
    '''正则表达式: . 代表一个除了换行符以外的所有字符'''
    print(re.findall('alex.a', 'r32432kalexXa89falexKasalexYafdsaffalex中a'))

def f2():
    '''正则表达式：^ 代表匹配的字符必须在开头'''
    print(re.findall('^alex', 'alex中a'))

def f3():
    '''正则表达式：$ 代表匹配的字符必须在结尾'''
    print(re.findall('alex$', 'fdsafdsafdsaalex'))

def f4():
    '''正则表达式：* 代表实现0次或多次匹配（贪婪匹配）'''
    print(re.findall('alex*', 'alxyeurealefdsafdsaalexfdsafalexfdsafdalexxxx'))

def f5():
    '''正则表达式：+ 代表实现1次或多次匹配（贪婪匹配）'''
    print(re.findall('alex+', 'alefdsafdsaalexfdsafalexfdsafdalexxxx'))

def f6():
    '''正则表达式：? 代表实现0次或1次匹配（非贪婪匹配）'''
    print(re.findall('ale?', 'alefdsafdsaalfdsafalexfdsafdalexxxx'))

def f7():
    '''正则表达式: . 代表一个除了换行符以外的所有字符'''
    print(re.findall('alex.a', 'r32432kalexXa89falexKasalexYafdsaffalex中a'))


def main():

    f7()





if __name__ == '__main__':
    main()