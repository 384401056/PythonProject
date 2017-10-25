#!/usr/bin/env python
# -*- coding utf-8 -*-

import socket

def main():
    client = socket.socket()
    client.connect(('127.0.0.1', 8002))
    print(str(client.recv(1024), encoding='utf-8'))
    client.close()

if __name__ == '__main__':
    main()