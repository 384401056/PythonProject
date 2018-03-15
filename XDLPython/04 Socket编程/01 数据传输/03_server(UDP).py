#!/usr/bin/env python
# -*- coding utf-8 -*-

import socket

def main():
    ''' UDP 服务器端， 不需要建立连接。'''

    # socket.AF_INET ipv4
    # socket.SOCK_DGRAM UDP
    ip_port = ('127.0.0.1', 8899)
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    sk.bind(ip_port)

    while True:
        # 阻塞
        data = sk.recv(1024)
        print(str(data, encoding='utf-8'))

if __name__ == '__main__':
    main()