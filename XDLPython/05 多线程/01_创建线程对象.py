#!/usr/bin/env python
# -*- coding utf-8 -*-
import threading
import time

# 线程执行的函数，target (也就是线程运行run的时候，执行的代码。)
def show(arg):
    time.sleep(1)
    print('thread' + str(arg))


def main():

    for i in range(10):
        t = threading.Thread(target=show, args=(i,))
        t.start()

    print('main thread stop')


if __name__ == '__main__':
    main()