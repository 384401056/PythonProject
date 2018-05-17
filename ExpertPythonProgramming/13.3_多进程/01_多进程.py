#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from multiprocessing import Process
import time

def work(identifier):
    print("hey ,I'm a process {}, pid:{}".format(identifier,os.getpid()))
    time.sleep(3)
    print("{} sleep over...".format(identifier))

def main():
    processes = [Process(target=work,args=(number,)) for number in range(5)]

    for process in processes:
        process.start()

    while processes:
        # 关闭进程
        processes.pop().join()


if __name__ == '__main__':
    main()