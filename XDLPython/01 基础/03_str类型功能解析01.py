#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    '''字符串'''
    a1 = 'alex is alph abc'
    # print(a1.capitalize()) # 首字母变大写
    # print(a1.center(20,'*')) # alex具中两边用*填充.
    # print(a1.count('a', 0, 15)) # 返回指定的字符在字符串中出现的次数。
    # print(a1.endswith('c')) # 判断字符串是否以给出的字符为结尾.
    # print(a1.startswith('a'))  # 判断字符串是否以给出的字符为开头.

    # content = 'hello\t999'
    # print(content)
    # print(content.expandtabs())# 将字符串中的TAB换为4个空格

    '''查找字符串'''
    # print(a1.find('is'))  # 查找字符串中的字符所在位置,没有找到返回-1
    # print(a1.index('q')) # 功能同上，只是没有找到就报错

    '''字符串格式化'''
    # s = 'hello {0}, age {1}'
    # print(s)
    # new1 = s.format('alex',19)
    # print(new1)

    '''字符串判断'''
    # s1 = 'ale/.x3239203dfeiwieowrj'
    # print(s1.isalnum()) # 判断字符串是不是字母和数据
    # s2 = ' '
    # print(s2.isspace()) # 判断字符是不是一个空格
    # s3 = 'This is Title'
    # print(s3.istitle()) # 判断字符串是不是一个标题
    # print('this is title'.title()) # 把字符串变为标题

    # li = ['gao', 'yan', 'bin']
    # s4 = '_'.join(li) # 用指定字符拼接列表类型字符
    # print(s4)

    '''去除空格'''
    s1 = '   alex   '
    # print(s1.lstrip()) # 去左
    # print(s1.rstrip()) # 去右
    # print(s1.strip())  # 去两边的

    '''分割'''
    s2 = 'alex SB alex'
    # print(s2.partition('SB')) # 保留分割的字符，返回原组
    # print(s2.split('e')) # 去除分割的字符,返回list
    # print(s2.split('e',1)) # 只分割第一个
    # s2 = 'alex\nSB\nalex\n'
    # print(s2.splitlines()) # 根据换行符进行分割

    '''替换'''
    # s2 = 'alex SB alex'
    # print(s2.replace('al','BB', 1)) # 1代表只替换从左第一个


def main2():
    '''索引'''
    s = 'alex'
    print(s[0])
    print(s[1])
    print(s[2])
    print(s[3])
    print(s[4])


def main3():
    '''切片'''
    s = 'alex'
    print(len(s)) # 获取长度
    print(s[0:2]) # 获取切片

    # 循环字符串
    for item in s:
        print(item)

if __name__ == '__main__':
    main3()
























