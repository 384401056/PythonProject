from twisted.internet import protocol, reactor
from time import ctime

HOST = 'localhost'
PORT = 9999

class TSClientProtocol(protocol.Protocol):

    def sendData(self):
        data = input('> ')
        if data:
            self.transport.write(data.encode())
        else:
            '''
            执行loseConnection()
            当发生这种情况时，将调用工厂的clientConnectionLost()方法以及停止reactor，结束脚本执行。
            '''
            self.transport.loseConnection()

    '''当客户端连接到服务器时就会执行connectionMade()方法'''
    def connectionMade(self):
        self.sendData()

    '''当收到通过网络发送的数据时就会调用dataReceived()方法'''
    def dataReceived(self, data):
        print(data.decode())
        self.sendData()

class TSClientFactory(protocol.ClientFactory):

    protocol = TSClientProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClientFactory())
reactor.run()