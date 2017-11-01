#!/usr/bin/env python
# -*- coding utf-8 -*-

from multiprocessing import Process
import threading
import time


def foo(i):
    time.sleep(1)
    print('say hi', i)


def main():
    for i in range(10):
        # 如果直接在主文件中去执行此代码，是无法运行的。只有在Linux下才可以.
        p = Process(target=foo, args=(i,))
        p.daemon = True  # 主进程不等待子进程执行。
        p.start()



    print('end')


if __name__ == '__main__':
    main()
