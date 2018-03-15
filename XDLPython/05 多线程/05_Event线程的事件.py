#!/usr/bin/env python
# -*- coding utf-8 -*-
import threading


def do(event, i):
    print('start ', i)
    event.wait()  # 产生阻塞(Event可以同时锁住所有的线程。)
    print('execute ', i)


event_obj = threading.Event()  # 创建event对象
for i in range(10):
    t = threading.Thread(target=do, args=(event_obj,i,))
    t.start()

print('判断是否可以断续执行子线程')
event_obj.clear()  # 所有线程将阻塞在event.wait().
# event_obj.set()  # 所有线程将不再阻塞.

inp = input('input:')
if inp == 'true':
    event_obj.set()  # 所有线程将不再阻塞.
