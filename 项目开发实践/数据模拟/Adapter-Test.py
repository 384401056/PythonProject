#!/usr/bin/env python
# -*- coding utf-8 -*-

import socket, ssl, time

HOST = ''
PORT = 10023
BUFSIZE = 1024
ADDR = (HOST, PORT)
# socket create success
bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket bind success
bindsocket.bind(ADDR)
# socket listen success
bindsocket.listen(5)


def do_something(connstream, data):
    return len(data)


def deal_with_client(connstream):
    data = connstream.recv(BUFSIZE)
    # empty data means the client is finished with us
    while data:
        backdata = do_something(connstream, data)
        if not backdata:
            # we'll assume do_something returns False
            # when we're finished with client
            break
        connstream.send(str(backdata))
        data = connstream.recv(BUFSIZE)


while True:
    newsocket, fromaddr = bindsocket.accept()
    print("socket accept one client from ", fromaddr)

    connstream = ssl.wrap_socket(newsocket, "key.pem", "cert.pem", server_side=True, ssl_version=ssl.PROTOCOL_TLSv1)

    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
