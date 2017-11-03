#!/usr/bin/env python
# -*- coding utf-8 -*-

import threading
import queue
import time

StopEven = object()


class MyThreadPool():
    '''自定义线程池'''

    def __init__(self, max_num=20):
        # 任务队列
        self.queue = queue.Queue(max_num)
        # 线程池最大容量。
        self.max_num = max_num
        # 总线程列表
        self.generate_list = []
        # 空闲线程列表
        self.freee_list = []

    def generate_thread(self):
        '''创建线程，并运行线程'''
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        '''获取任务函数，并执行任务.'''
        # 获取当前的线程。加入线程列表
        current_thread = threading.current_thread()
        self.generate_list.append(current_thread)
        print(current_thread.name, ' generate size', len(self.generate_list))

        event = self.queue.get()  # 从队列获取任务对象, 会产生阻塞

        # 如果获取到的event不是StopEven，则执行循环体。
        while event != StopEven:
            func, arguments, callback = event
            try:
                result = func(*arguments)  # 执行任务对象的func,并传入参数。如果是多个参数，则func函数的参数要加*
                status = True
            except Exception as ex:
                status = False
                result = ex
            if callback is not None:
                try:
                    callback(status, result)
                except Exception as ex:
                    pass

            self.freee_list.append(current_thread)
            event = self.queue.get()  # 从队列获取任务对象, 会产生阻塞
            self.freee_list.remove(current_thread)  # 如果从任务队伍中获取到数据，则将当前线程从free_list中删除
            print('generate size', len(self.generate_list))
        else:
            self.generate_list.remove(current_thread)

    def run(self, func, args, callback):
        '''执行任务'''
        w = (func, args, callback)
        # 将任务放入任务队列
        self.queue.put(w)

        # 如果除于线程数为0并且线程总线小于总线程数，则创建线程
        if len(self.freee_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()


def work(i):
    try:
        print('任务 ', i)
        return True
    except Exception as ex:
        return False


def down(status, result):
    print('callbacke down')


def main():
    pool = MyThreadPool(10)
    for i in range(100):
        pool.run(func=work, args=(i,), callback=down)


if __name__ == '__main__':
    main()
