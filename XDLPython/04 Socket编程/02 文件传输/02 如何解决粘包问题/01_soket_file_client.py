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

    # 发送完文件大小的信息后，等待接收服务器端的回应.
    # 如果有回应或者回应正常，才发送文件数据。
    response = client.recv(1024)
    print(str(response, encoding='utf-8'))
    if int(str(response, encoding='utf-8')) == file_size:

        with open('01.jpg', 'rb') as f:
            # 循环发送文件内容。
            for line in f:
                client.sendall(line)

        client.close()

if __name__ == '__main__':
    main()
