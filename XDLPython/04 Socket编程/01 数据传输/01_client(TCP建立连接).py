#!/usr/bin/env python
# -*- coding utf-8 -*-
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8899))  # 连接服务器
    client.close()  # 关闭连接


if __name__ == '__main__':
    main()