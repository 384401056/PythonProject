#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
通过描述符，实现懒加载。
"""


class InitOnAccess(object):
    def __init__(self, klass, *args, **kwargs):
        self.klass = klass
        self.args = args
        self.kwargs = kwargs
        self._initialized = None


    def __get__(self, instance, owner):
        if self._initialized is None:
            print("initialized!")
            self._initialized = self.klass(*self.args, **self.kwargs)
        else:
            print("cached")
        print(self._initialized)
        return self._initialized


class MyClass(object):
    lazily_initialized = InitOnAccess(list, "ARGUMENT")


def main():
    m = MyClass()
    m.lazily_initialized #第一次执行时，对_initialized加载数据。

    m.lazily_initialized #第二次执行时，直接取值。

if __name__ == '__main__':
    main()