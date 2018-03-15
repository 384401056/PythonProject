#!/usr/bin/env python
# -*- coding utf-8 -*-
import pickle


def f1(date):
    '''使用字符串和bytes之间的转换来存储字典数据'''
    bt = bytes(str(date), 'utf-8')
    print(bt)
    with open('test01.txt', 'wb+') as f:
        f.write(bt)

def f2(date):
    '''使用 pickle 的方法来存储字典数据 '''
    bt = pickle.dumps(date)
    print(bt)
    with open('test02.txt', 'wb+') as f:
        f.write(bt)

def f3():
    '''使用普通的方法从文件中读取字典数据'''
    '''此时，取到的数据只是字符串'''
    with open('test01.txt', 'rb+') as f:
        ret = f.read()
    return ret

def f4():
    '''使用pickle.loads来进行取数据'''
    '''此时，取到的数据是字典对象'''
    with open('test02.txt', 'rb+') as f:
        ret = pickle.loads(f.read())
    return ret


def main():
    date = {
        1000:{'name': 'jim', 'age': 10, 'class':1},
        2000:{'name': 'lily', 'age': 20, 'class':2},
        3000:{'name': 'kimy', 'age': 30, 'class':3}
    }


    ret_dict = f4()
    ret_dict[1000]['age'] += 100 # 找到age, 对其加100
    print(ret_dict[1000])


if __name__ == '__main__':
    main()