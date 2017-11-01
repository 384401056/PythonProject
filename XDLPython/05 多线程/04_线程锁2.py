#!/usr/bin/env python
# -*- coding utf-8 -*-
import threading
import time


# 定义全局变量
gl_num = 0

lock = threading.RLock()


def show(arg):
    # 加锁
    lock.acquire()

    # 对全局变量进行操作
    global gl_num
    time.sleep(1)
    gl_num += 1
    print("running on number:%s" % arg, gl_num)

    lock.release()


def main():

    for i in range(100):
        t = threading.Thread(target=show, args=(i,))
        t.start()

    print('main thread stop')


if __name__ == '__main__':
    main()