#!/usr/bin/env python
# -*- coding utf-8 -*-

import threading
import time


def show(arg):
    time.sleep(1)
    print("running on number:%s" % arg)


def main():
    for i in range(100):
        t = threading.Thread(target=show, args=(i,))
        t.start()

    print('main thread stop')

if __name__ == '__main__':

    # 最多允许5个线程同时运行
    semaphore = threading.BoundedSemaphore(5)
    main()