#!/usr/bin/env python
# -*- coding utf-8 -*-

import threading
import queue
import time

class MyThreadPool():
    '''自定义线程池'''

    def __init__(self, max_num=20):
        self.queue = queue.Queue(max_num)
        for i in range(max_num):
            self.queue.put(threading.Thread) # 将线程类的类名放入队列中

    def get_thread(self):
        '''获取线程'''
        return self.queue.get()

    def add_thread(self):
        '''新增线程'''
        self.queue.put(threading.Thread)


def f1(pool):
    time.sleep(1)
    print('thread func')
    pool.add_thread()


def main():
    pool = MyThreadPool(5)

    for i in range(20):
        thread = pool.get_thread()
        t = thread(target=f1, args=(pool,))
        t.start()


if __name__ == '__main__':
    main()
