#!/usr/bin/env python
# -*- coding utf-8 -*-

import socket
import os


def main():

    # 连接服务器
    client = socket.socket()
    client.connect(('127.0.0.1', 8899))

    # 获取要上传的文件大小.
    file_size = os.stat('01.jpg').st_size
    # 先发送文件大小的数据到服务器。
    client.sendall(bytes(str(file_size), encoding='utf-8'))

    with open('01.jpg', 'rb') as f:
        # 循环发送文件内容。
        for line in f:
            client.sendall(line)

    client.close()

if __name__ == '__main__':
    main()
