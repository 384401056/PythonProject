#!/usr/bin/env python
# -*- coding utf-8 -*-

import abc


# 抽象类
class AbsUser(metaclass=abc.ABCMeta):

    def func1(self):
        print('func1')

    # 抽象方法
    @abc.abstractmethod
    def func2(self):
        """
        定义了一个抽象方法
        :return:
        """


class User(AbsUser):
    """
    此类继承了抽象类。所以要实现父类中的抽象方法。否则实例化时会报错。
    """
    # def func2(self):
    #     print('func2')


def main():
    user = User()
    user.func1()
    user.func2()


if __name__ == '__main__':
    main()
