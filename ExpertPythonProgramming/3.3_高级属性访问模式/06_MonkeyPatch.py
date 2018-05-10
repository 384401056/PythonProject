#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Foo(object):
    def bar(self):
        print("Foo.bar")

def bar(self):
    print("Modified bar")



def main():
    Foo().bar()
    Foo.bar = bar
    Foo().bar()

if __name__ == '__main__':
    main()