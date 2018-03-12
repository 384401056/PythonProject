#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta
from abc import abstractmethod


class Father(metaclass=ABCMeta):  # 创建抽象类

    @abstractmethod
    def f1(self):
        pass

    @abstractmethod
    def f2(self):
        pass

    @abstractmethod
    def f3(self):
        pass


class F1(Father):

    def f1(self):
        pass

    def f2(self):
        pass

    def f3(self):
        pass

def main():
    f = F1()
    f.f1()


if __name__ == '__main__':
    main()