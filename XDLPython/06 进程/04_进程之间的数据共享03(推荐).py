#!/usr/bin/env python
# -*- coding utf-8 -*-

from multiprocessing import Process, Array, Manager
from threading import Thread
import time


# Array是一种特殊的数据结构，可用于进程间的数据共享.
# 其中第一个参数 i 指数据类型为int


def func(i, dic):
    # dic[i] = 100 + i
    # print(i, '----->', len(dic))

    dic[i] = 100 + i
    for k, v in dic.items():
        print(k, v)
    print('-----')


if __name__ == '__main__':
    manager = Manager()
    dic = manager.dict()
    # dic = {}

    for i in range(2):
        p = Process(target=func, args=(i, dic,))
        p.start()
        # 主进程等待子进程结束.
        # p.join()
    time.sleep(3)
    print('main Process')
