#!/usr/bin/env python
# -*- coding utf-8 -*-

import socket
import select

def main():
    sk1 = socket.socket()
    sk1.bind(('127.0.0.1', 8001))
    sk1.listen()

    sk1.accept()

    sk2 = socket.socket()
    sk2.bind(('127.0.0.1', 8002))
    sk2.listen()

    sk_list = [sk1, sk2,]

    while True:
        # select 监视多个描述符[sk1, sk2,], 一旦描述符发生变化，就会在返回的r_list中加入该描述符
        r_list, w_list, e_list = select.select(sk_list, [], [], 1)

        # 循环r_list列表，来 accept() 多个端口
        for sk in r_list:
            conn, address = sk.accept()
            conn.sendall(bytes('Hello Client, Im server!', encoding='utf-8'))
            print(str(address))

            conn.close()

if __name__ == '__main__':
    main()