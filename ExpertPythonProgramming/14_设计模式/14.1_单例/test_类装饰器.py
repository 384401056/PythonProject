#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Decorator(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("decorator start")
        self.f()
        print("decorator end")

@Decorator
def func():
    print("func")


def main():
    func()


if __name__ == '__main__':
    main()