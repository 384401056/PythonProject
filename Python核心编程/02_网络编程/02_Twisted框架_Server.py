from twisted.internet import protocol, reactor
from time import ctime

PORT = 9999

class TSServerProtocol(protocol.Protocol):
    '''
    我们获得protocol 类并为时间戳服务器调用TSServProtocol。然后重写了connectionMade()
    和dataReceived()方法
    '''

    '''当一个客户端连接到服务器时就会执行connectionMade()方法'''
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('连接来自:',clnt)

    '''当服务器接收到客户端通过网络发送的一些数据时就会调用dataReceived()方法'''
    def dataReceived(self, data):
        self.transport.write(('[%s] %s' % (ctime(),data)).encode())

'''
创建了一个协议工厂。它之所以被称为工厂，是因为每次
得到一个接入连接时，都能“制造”协议的一个实例。然后在reactor 中安装一个TCP 监听
器，以此检查服务请求。当它接收到一个请求时，就会创建一个TSServProtocol 实例来处理
那个客户端的事务
'''
factory = protocol.Factory();
factory.protocol = TSServerProtocol
print('等待连接.....')
reactor.listenTCP(PORT, factory)
reactor.run()
