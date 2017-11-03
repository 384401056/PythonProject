#!/usr/bin/env python
# -*- coding utf-8 -*-



args = ('aaa',)


def func(arg):
    print(arg)

def aaa(f, args):
    # print(*args)
    f(args)


def main():
    aaa(func, args)


if __name__ == '__main__':
    main()
