''' socketserver模块的使用 '''
from socketserver import TCPServer as tcp, StreamRequestHandler
from time import ctime

HOST = 'localhost'
PORT = 9999
ADDR = (HOST, PORT)

class MyRequestHandler(StreamRequestHandler):
    '''
    请求处理程序
    当接收到一个来自客户端的消息时，它就会调用handle()方法。而StreamRequestHandler
    类将输入和输出套接字看作类似文件的对象，因此我们将使用readline()来获取客户端消息，
    并利用write()将字符串发送回客户端。

    SocketServer 请求处理程序的默认行为是接受连接、获取请求，然后关闭连接。
    所以客户端的连接每次都要重新建立。除非在handle()方法中使用循环.
    '''

    def handle(self):
        ''' 重写了它的handle()方法，该方法在基类Request中,默认情况下没有任何行为。 '''
        # print('连接来自于：',self.client_address)
        # readStr = self.rfile.readline()
        # writeStr = '[%s] %s' % (ctime(), readStr)
        # self.wfile.write(writeStr.encode('utf-8'))

        ''' 在handle()方法中使用循环，让Server可保持连接 '''
        print('连接来自于：',self.client_address)
        while True:
            try:
                readStr = self.rfile.readline()
                if not readStr:
                    break
                writeStr = '[%s] %s' % (ctime(), readStr)
                self.wfile.write(writeStr.encode('utf-8'))
            except Exception as e:
                print(e)
                break

tcpServer = tcp(ADDR,MyRequestHandler)
print("等待连接....")
tcpServer.serve_forever()
