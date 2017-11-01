#!/usr/bin/env python
# -*- coding utf-8 -*-

from multiprocessing import Process
import threading
import time


def foo(i):
    print('say hi', i)


def main():
    for i in range(10):
        # 如果直接在主文件中去执行此代码，是无法运行的。只有在Linux下才可以.
        p = Process(target=foo, args=(i,))
        p.start()

    print('end')

if __name__ == '__main__':
    main()