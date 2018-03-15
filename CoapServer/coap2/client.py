#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coapthon.client.helperclient import HelperClient
import time

def main():
    host = "47.104.162.6"
    # host = "127.0.0.1"
    port = 9800
    path = "/api/v1"

    # for i in range(10):
    # print 'i %d' % i
    # time.sleep(1)
    client = HelperClient(server=(host, port))
    # response = client.post(path=path, payload=bytearray(['A', 'S', 'B', 'E', 'F']))
    response = client.post(path=path, payload='gaoyanbin')
    # response = client.get(path=path)
    print response.pretty_print()
    client.close()




if __name__ == '__main__':
    main()