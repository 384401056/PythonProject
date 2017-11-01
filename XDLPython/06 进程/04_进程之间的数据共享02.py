#!/usr/bin/env python
# -*- coding utf-8 -*-

from multiprocessing import Process, Array
from threading import Thread
import time


def func(i, temp):
    temp[i] = 100 + temp[i]
    for item in temp:
        print(i, '----->', item)


if __name__ == '__main__':

    # Array是一种特殊的数据结构，可用于进程间的数据共享.
    # 其中第一个参数 i 指数据类型为int
    temp = Array('i', [11, 22, 33, 44, 55])

    for i in range(2):
        p = Process(target=func, args=(i, temp,))
        p.start()
        p.join()

    print('main Process')
