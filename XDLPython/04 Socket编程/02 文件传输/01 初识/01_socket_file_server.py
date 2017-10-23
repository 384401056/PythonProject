#!/usr/bin/env python
# -*- coding utf-8 -*-

import socket
import time


def main():
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8899))
    sk.listen(10)
    while True:
        conn, address = sk.accept()
        # 接收文件大小
        file_size = int(str(conn.recv(1024), encoding='utf-8'))
        has_size = 0
        print(file_size, address)

        with open('new_'+str(time.time())+'.jpg', 'wb') as f:

            # 循环接收文件内容。
            while True:
                # 根据文件大小来判断是否已经接收完成。
                if has_size == file_size:
                    break
                data = conn.recv(1024)
                f.write(data)
                has_size += len(data)

        conn.close()

if __name__ == '__main__':
    main()
