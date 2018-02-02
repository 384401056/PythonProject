#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coapthon.client.helperclient import HelperClient
import time

def main():
    host = "118.190.43.87"
    # host = "127.0.0.1"
    port = 5683
    path = "t"

    for i in range(10):
        print 'i %d' % i
        time.sleep(1)
        client = HelperClient(server=(host, port))
        response = client.post(path=path, payload=bytearray(['A', 'S', 'B', 'E', 'F']))
        # response = client.put(path=path, payload='gaoyanbin')
        # response = client.get(path=path)
        print response.pretty_print()
    client.close()




if __name__ == '__main__':
    main()