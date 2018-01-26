#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from time import ctime

HOST = 'fe80::e030:771e:4a5e:eb04'
PORT = 21567
BUFSIZ = 1024

tcpSerSock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
tcpSerSock.bind((HOST, PORT))
# tcpSerSock.bind((HOST, PORT, 0, 2)) # 在linux下运行时.
tcpSerSock.listen(5)

while True:
    print('Waiting for connection....')
    try:
        tcpCliSock, cliAddr = tcpSerSock.accept()
        print(cliAddr)
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            print(str(data, encoding='utf-8'))

            # tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode())

            msg = '[%s] %s' % (ctime(), data.decode('utf-8'))
            tcpCliSock.send(bytes(msg, encoding='utf-8'))
        tcpCliSock.close()
    except Exception as ex:
        print(ex)