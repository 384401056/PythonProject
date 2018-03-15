#!/usr/bin/env python
# -*- coding utf-8 -*-
import socket


def main():
    ''' 建立连接 参数可省略'''
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET 代表ipv4协议簇，SOCK_STREAM 代表TCP.
    sk.bind(('127.0.0.1', 8899))
    sk.listen(10)

    while True:
        # 等待接收客服端连接， accept 方法会阻塞
        conn, address = sk.accept()
        print(conn)
        print(address)
        conn.sendall(bytes("Hello socket!", encoding='utf-8'))


if __name__ == '__main__':
    main()