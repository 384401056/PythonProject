#!/usr/bin/env python
# -*- coding utf-8 -*-

import contextlib  # 上下文管理模块
import queue

q = queue.Queue()
li = ['alex']


@contextlib.contextmanager
def work_state(li, val):
    '''定义一个上下文管理方法'''
    li.append(val)  # 进入上下方法执行此句
    try:
        yield
    finally:
        li.remove(val)  # 离开上下文方法执行此句


def main():

    # print(li)
    # li.append('gaoyanbin')
    # print(li)
    # li.remove('gaoyanbin')
    # print(li)

    # 下面的执行结，同上面的代码。使用with 上下文管理可以优化代码结构。
    print(li)
    with work_state(li, 'gaoyanbin'):
        print(li)
    print(li)







if __name__ == '__main__':
    main()
