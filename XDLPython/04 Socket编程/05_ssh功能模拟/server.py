#!/usr/bin/env python
# -*- coding utf-8 -*-

import socketserver
import subprocess


class MyServer(socketserver.BaseRequestHandler):
    # 当有客户端连接到服务器时，就会执行此段代码.
    def handle(self):
        print('client connect!')
        conn = self.request  # 获取conn连接
        client_address = self.client_address  # 客户端地址
        server = self.server  # server实例

        while True:  # 循环的接收数据
            try:
                total_size = 0
                cmd = str(conn.recv(1024), encoding='utf-8')
                cmd_lsit = cmd.split(' ')
                print(cmd_lsit)
                if cmd_lsit[0] == 'exit':
                    break

                cmd_bytes = subprocess.check_output(cmd_lsit, shell=True)  # 执行系统命令，返回执行结果(bytes类型)
                total_size = len(cmd_bytes)

                # 如果执行命令的返回值小于等于0，则认为执行失败
                if total_size <= 0:
                    conn.sendall(bytes(str('0'), encoding='utf-8'))
                    continue
                else:
                    conn.sendall(bytes(str(total_size), encoding='utf-8'))

                ret = str(conn.recv(1024), encoding='utf-8')
                if ret == 'ok':
                    print(total_size)
                    conn.sendall(cmd_bytes)

            # 客户端断开连接
            except ConnectionResetError as ex:
                print(ex)
                # 退出接收数据的循环体
                break
            # 命令执行出错。则返回字节数为0.
            except (OSError, subprocess.CalledProcessError) as ex:
                conn.sendall(bytes(str('0'), encoding='utf-8'))
                print(ex)
            # 其它原因造成的命令无法执行，则返回字节数为0.
            except Exception as ex:
                conn.sendall(bytes(str('0'), encoding='utf-8'))
                print(ex)

        conn.close()


def main():
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8899), MyServer)
    server.serve_forever()  # 循环


if __name__ == '__main__':
    main()
