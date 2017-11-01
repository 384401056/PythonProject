#!/usr/bin/env python
# -*- coding utf-8 -*-
import threading
import time


def show(arg):
    time.sleep(1)
    print('thread' + str(arg))


def main():
    for i in range(10):
        t = threading.Thread(target=show, args=(i,))
        t.setDaemon(True)  # 此值为True时，主线程结束就结束，不会等待子线程。
        t.start()

    time.sleep(1)  # 相当于主线程的耗时操作。
    print('main thread stop')  # 只会输入6或者8个线程，还有2个被强行终止了。


if __name__ == '__main__':
    main()
