#!/usr/bin/env python
# -*- coding utf-8 -*-


NUM = 100


def fun1():
    global NUM
    print(NUM)
    NUM = 200

def fun2():
    print(NUM)


def main():
    fun1()
    fun2()


if __name__ == '__main__':
    main()