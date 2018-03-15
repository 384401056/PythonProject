#!/usr/bin/env python
# -*- coding utf-8 -*-
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        time.sleep(1)
        print("running on number:%s" % self.num)


def main():

    for i in range(10):
        t = MyThread(i)
        t.start()

    print('main thread stop')


if __name__ == '__main__':
    main()
