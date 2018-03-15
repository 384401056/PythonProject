#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
# ADDR = (HOST, PORT, 0, 2) # 的linux下运行时

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    tcpCliSock.connect(ADDR)
    while True:
        data = input('>')
        if not data:
            break
        tcpCliSock.send(bytes(data, encoding='utf-8'))
        retData = tcpCliSock.recv(BUFSIZ)
        if not retData:
            break
        print(retData.decode('utf-8'))
except Exception as ex:
        print(ex)

