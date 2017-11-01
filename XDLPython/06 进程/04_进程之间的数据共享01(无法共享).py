#!/usr/bin/env python
# -*- coding utf-8 -*-

from multiprocessing import Process
from threading import Thread
import time

li = []

def func(arg):

    li.append(arg)
    print('Process %d %s' % (arg, li))


def main():
    for i in range(10):
        # 对于进程来说，所有变量都会自建一份。所以每个进程操作的都是自己的li.
        p = Process(target=func, args=(i,))
        p.start()

        # 对于线程来说，变量是可以共享，所以所有线程的操作都是针对一个li进行的。
        # t = Thread(target=func, args=(i,))
        # t.start()

if __name__ == '__main__':
    main()
