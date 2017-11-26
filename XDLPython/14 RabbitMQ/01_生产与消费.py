#!/usr/bin/env python
# -*- coding utf-8 -*-

import queue
import threading

message = queue.Queue()


def producer():
    for item in range(50):
        message.put(item)
        print('produce', item)


def consumer():
    while True:
        msg = message.get() # 当队列中没有数据时，会阻塞.
        print('consumer',msg)


def main():

    t1 = threading.Thread(target=producer)
    t1.start()

    t2 = threading.Thread(target=consumer())
    t2.start()


if __name__ == '__main__':
    main()
