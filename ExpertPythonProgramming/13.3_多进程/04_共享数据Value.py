#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Value, Array

def work(num, arr):
    print("CHLD: {}".format(num.value))
    print("CHLD: {}".format(arr[:]))

    # 在子进程中修改共享数据的值。
    num.value = 3.1415926
    for i in range(len(arr)):
        arr[i] = -arr[i]


def main():
    # 共享数据
    num = Value('d', 0.01) # 值
    arr = Array('i', range(10)) # 数组

    child = Process(target=work, args=(num, arr,)) # 将共享数据做为参数传入子进程。

    child.start()
    child.join()

    print("PARENT: {}".format(num.value))
    print("PARENT: {}".format(arr[:]))

if __name__ == '__main__':
    main()