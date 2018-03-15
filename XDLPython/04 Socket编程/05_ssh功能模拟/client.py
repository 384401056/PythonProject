#!/usr/bin/env python
# -*- coding utf-8 -*-

import socket

def main():

    # 连接服务器
    client = socket.socket()
    client.connect(('127.0.0.1', 8899))

    buffer_size = 0;
    while True:
        try:
            inp = input("输入系统命令：")
            if inp == 'exit':
                client.sendall(bytes(inp, encoding='utf-8'))
                break
            else:
                client.sendall(bytes(inp, encoding='utf-8'))
                ret = client.recv(1024)
                buffer_size = int(str(ret, encoding='utf-8'))
                # 如果命令返回的字节数为0，则说明执行出错。
                if buffer_size <= 0:
                    print("命令错误")
                    continue
                else:
                    # 发送确认信息
                    client.sendall(bytes('ok', encoding='utf-8'))
                    # 重新设备缓冲区大小,并开始接收后面的数据
                    ret_bytes = client.recv(buffer_size)
                    try:
                        print(str(ret_bytes, encoding='gbk'))
                    except UnicodeDecodeError:
                        print(str(ret_bytes, encoding='utf-8'))
        except Exception as ex:
            print(ex)

    client.close()


if __name__ == '__main__':
    main()