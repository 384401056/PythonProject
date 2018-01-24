#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop

class MySocketServer(TCPServer):

    def listen(self, port, address=""):
        super().listen(port, address)
        print('Server start......')

    def handle_stream(self, stream, address):
        print('connected client:', address)
        stream.read_until('\n', callback=self.send_message)

    def send_message(self,data):
        print(data)



if __name__ == '__main__':
    server = MySocketServer()
    server.listen(21567)
    IOLoop.instance().start()
