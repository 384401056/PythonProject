#!/usr/bin/env python
# -*- coding utf-8 -*-

class Person:

    __mydict = dict()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        value = self.__mydict[item]
        print(value)

    def __setitem__(self, key, value):
        self.__mydict[key] = value

    def __delitem__(self, key):
        # 如果key存在，则删除__mydict中对象的key
        if key in self.__mydict.keys():
            del(self.__mydict[key])
            print('del success')

def main():
    person = Person('jim',20)

    # 用字典key的形式，访问了对象并赋值.会执行类中的__setitem__方法.
    person['aaa'] = 333
    person['kkk'] = 'myname'

    # 用字典key的形式，访问对象会执行类中的__getitem__方法.
    person['aaa']
    person['kkk']

    # 用字典的形式，del对象中的key,会执行类中的__delitem__方法
    del person['kkk']

    person['kkk'] # 报错，kkk已经被删除


if __name__ == '__main__':
    main()