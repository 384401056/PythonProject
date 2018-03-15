#!/usr/bin/env python
# -*- coding utf-8 -*-

from multiprocessing import Process, Pool
import time


def f1(i):
    time.sleep(1)
    # print(i)
    return i # func的返回值就是callback的参数


def f2(args):
    print(args)


if __name__ == '__main__':

    pool = Pool(5)  # 定义进程池，并设置最大进程数。

    for i in range(40):
        # 开启进程
        # pool.apply(func=func01, args=(i,))
        pool.apply_async(func=f1, args=(i,), callback=f2)  # 并发执行进程，并可以设置回调函数。

    pool.close()
    pool.join()
    print('pool end')
