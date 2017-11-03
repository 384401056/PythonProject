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
        # 生成的线程列表
        self.generate_list = []
        # 空闲线程列表
        self.freee_list = []

    def generate_thread(self):
        '''创建线程，并运行线程'''
        t = threading.Thread(target=self.call)
        t.start()


    def close(self):
        '''关闭 self.queue.get() 等待的方法'''
        # 根据当前的线程数生成StopEven对象，放入任务队列。
        num = len(self.generate_list)
        while num:
            self.queue.put(StopEven)
            num -= 1

    def call(self):
        '''获取任务函数，并执行任务.'''
        # 获取当前的线程。加入线程列表
        current_thread = threading.current_thread()
        self.generate_list.append(current_thread)


        event = self.queue.get()  # 从队列获取任务对象, 会产生阻塞

        print(current_thread.name, ' generate size', len(self.generate_list))

        # 如果获取到的event不是StopEven，则执行循环体。
        while event != StopEven:
            func, arguments, callback = event
            try:
                # 执行任务对象的func,并传入参数。如果是多个参数，则func函数的参数要加*,arguments传入的是元组。
                # *arguments传的是一个一个的参数
                result = func(*arguments)
                status = True
            except Exception as ex:
                status = False
                result = ex
            if callback is not None:
                try:
                    callback(current_thread.name,status, result)
                except Exception as ex:
                    pass

            self.freee_list.append(current_thread)
            event = self.queue.get()  # 从队列获取任务对象, 会产生阻塞
            self.freee_list.remove(current_thread)  # 如果从任务队伍中获取到数据，则将当前线程从free_list中删除
            # print('generate size', len(self.generate_list))
        else:
            self.generate_list.remove(current_thread)

        self.close()

    def run(self, func, args, callback):
        '''执行任务'''
        w = (func, args, callback)
        # 将任务放入任务队列
        self.queue.put(w)

        # 如果空亲线程数为0并且线程总线小于总线程数，则创建线程
        if len(self.freee_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()



def work(i):
    try:
        print('任务 ', i)
        return True
    except Exception as ex:
        return False


def down(threadname, status, result):
    print('callbacke down ', threadname)


def main():
    pool = MyThreadPool(10)
    for i in range(101):
        pool.run(func=work, args=(i+1,), callback=down)


if __name__ == '__main__':
    main()
