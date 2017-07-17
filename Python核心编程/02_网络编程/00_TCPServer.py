''' socket 模块函数 '''
# from socket import socket

# # 创建TCP/IP 套接字
# tcpSock = socket(AF_INET, SOCK_STREAM)
#
# # 了创建UDP/IP 套接字
# udpSock = socket(socket.AF_INET, socket.SOCK_DGRAM)

''' 一个TCP 时间戳服务器 '''
from socket import *
from time import ctime

HOST = 'localhost'
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST,PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(ADDR)
serverSocket.listen(5)

while True:
    try:
        print('等待连接....')
        clientSocket,clientAddr = serverSocket.accept();
        print("连接来自 %s" % str(clientAddr))

        # 循环接收数据
        while True:
            data = clientSocket.recv(BUFSIZ).decode('UTF-8')
            if not data:
                break
            print(data)
            clientSocket.send(('[%s] %s' % (ctime(),'This is from server!')).encode())
        clientSocket.close()
    except:
        break
serverSocket.close()
