#!/usr/bin/env python
# -*- coding utf-8 -*-
import pickle


def f1():
    date = {
        1000: {'name': 'jim', 'age': 10, 'class': 1},
        2000: {'name': 'lily', 'age': 20, 'class': 2},
        3000: {'name': 'kimy', 'age': 30, 'class': 3}
    }

    with open('test01.json', 'wb') as f:
        pickle.dump(date, f)


def f2():
    with open('test01.pk', 'rb') as f:
        '''用load直接返回对象'''
        ret_dict = pickle.load(f)
        print(type(ret_dict))
        print(ret_dict[2000])


def main():

    f2()


if __name__ == '__main__':
    main()