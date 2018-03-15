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
        t.start()
        t.join()  # 让主线程等待，子线程结束才继续往下执行。可指定最长等待时间。
        print('i=%d' % i)

    print('main thread stop')


if __name__ == '__main__':
    main()
