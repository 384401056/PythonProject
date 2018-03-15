#!/usr/bin/env python
# -*- coding utf-8 -*-
import threading
import time


# 定义全局变量
gl_num = 0

lock = threading.RLock()

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        # 获得锁
        lock.acquire()

        # 对全局变量进行操作
        global gl_num
        time.sleep(1)
        gl_num += 1
        print("running on number:%s" % self.num, gl_num)

        # 解锁
        lock.release()


def main():

    for i in range(10):
        t = MyThread(i)
        t.start()

    print('main thread stop')


if __name__ == '__main__':
    main()
