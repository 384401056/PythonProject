#!/usr/bin/env python
# -*- coding utf-8 -*-
import socket

def main():
    ''' 相互发送数据'''
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8899))
    sk.listen(10)

    while True:
        # 等待接收客服端连接， accept 方法会阻塞
        conn, address = sk.accept()

        try:
            while True:  # 循环的接收数据
                ret = conn.recv(1024)
                msg = str(ret, encoding='utf-8')
                if msg == 'exit':
                    break
                else:
                    print(msg)
                    conn.sendall(bytes(msg + " ....", encoding='utf-8'))
        except Exception as ex:
            print(ex)
            conn.close()


if __name__ == '__main__':
    main()