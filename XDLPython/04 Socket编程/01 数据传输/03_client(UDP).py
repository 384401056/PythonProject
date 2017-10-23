#!/usr/bin/env python
# -*- coding utf-8 -*-
import socket

def main():
    ip_port = ('127.0.0.1', 8899)
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    while True:
        inp = input('请输入要发送的数据:').strip()
        if inp == 'exit':
            break
        sk.sendto(bytes(inp, encoding='utf-8') , ip_port)

    sk.close()


if __name__ == '__main__':
    main()