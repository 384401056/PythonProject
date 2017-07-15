''' TCP 客户端'''
import sys
from socket import *

HOST = 'localhost'
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)

while True:
    try:
        data = input('> ')
        if not data:
            break
        # 为发送的数据加上回车换行，并转为bytes
        clientSocket.send(('%s\r\n' % data).encode())

        data = clientSocket.recv(BUFSIZ)
        if not data:
            break
        print(data.decode())
    except Exception as e:
        print(e)
        break

clientSocket.close()

