#!/usr/bin/env python
# -*- coding utf-8 -*-

'''生成器的作用：保存函数的执行状态。'''


def myBuilder():

    print('11111')
    print('11111')
    yield 1

    print('22222')
    print('22222')
    yield 2

    print('33333')
    print('33333')
    yield 3



def main():

    # 获取到一个生成器对象
    mb = myBuilder()

    # 执行生成器
    ret = mb.__next__()
    print(ret)

    ret = mb.__next__()
    print(ret)


if __name__ == '__main__':
    main()