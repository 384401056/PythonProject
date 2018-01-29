#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coapthon.client.helperclient import HelperClient

def main():
    # host = "118.190.43.87"
    host = "127.0.0.1"
    port = 5683
    path = "t"

    client = HelperClient(server=(host, port))
    response = client.post(path=path, payload= bytearray('Hello CoapServer!', 'utf-8'))
    # response = client.put(path=path, payload='gaoyanbin')
    # response = client.get(path=path)

    print response.pretty_print()
    client.stop()


if __name__ == '__main__':
    main()