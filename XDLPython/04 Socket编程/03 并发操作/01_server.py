#!/usr/bin/env python
# -*- coding utf-8 -*-

import socketserver


class MyServer(socketserver.BaseRequestHandler):

    # 当有客户端连接到服务器时，就会执行此段代码.
    def handle(self):
        conn = self.request  # 服务器连接
        client_address = self.client_address  # 客户端地址
        # server = self.server  # server实例
        try:
            while True:  # 循环的接收数据
                ret = conn.recv(1024)
                msg = str(ret, encoding='utf-8')
                if msg == 'exit':
                    break
                else:
                    # 打印客户端信息
                    client_info = 'From: %s' % str(client_address)
                    print(client_info, ': ', msg)
                    conn.sendall(bytes(msg + " ....(来自服务器的回复)", encoding='utf-8'))
        except Exception as ex:
            print(ex)
            conn.close()


def main():
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8899), MyServer)
    server.serve_forever()  # 循环


if __name__ == '__main__':
    main()
