#!/usr/bin/env python
# -*- coding utf-8 -*-

import socket

def main():
    client = socket.socket()
    client.connect(('127.0.0.1', 8899))  # 连接服务器

    try:
        while True:  # 循环的发送数据
            mes = input("输入要发送的信息:")
            if mes != 'exit':
                client.sendall(bytes(mes, encoding='utf-8'))
                result = client.recv(1024)
                print(str(result, encoding='utf-8'))
            else:
                client.sendall(bytes(mes, encoding='utf-8'))
                break
    except Exception as ex:
        print(ex)
        client.close()


if __name__ == '__main__':
    main()