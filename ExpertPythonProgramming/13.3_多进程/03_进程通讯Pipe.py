#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Pipe


def work(connection):
    while True:
        instance = connection.recv()
        if instance:
            print("CHLD recv: {}".format(instance))
        else:
            return


class CustomClass(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    parent_conn, child_conn = Pipe()  # 创建主进程与子进程的通讯连接

    child = Process(target=work, args=(child_conn,))  # 将通讯连接做为子进程的参数

    child.start()

    # 向子进程中循环传递数据。
    for item in (
            42,
            'some string',
            {"one",1},
            (1,2,3,4,5),
            CustomClass("kkk",100),
            None,
    ):
        print("PARENT send: {}".format(item))
        parent_conn.send(item)

    child.join()

if __name__ == '__main__':
    main()
