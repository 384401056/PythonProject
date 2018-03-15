#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coapthon.client.helperclient import HelperClient

# host = "118.190.43.87"
# host = "127.0.0.1"
# port = 5683
# path ="t/"

host = "47.104.162.6"
port = 9800
path = "/api/v1"

client = HelperClient(server=(host, port))
# response = client.post(path=path, payload='1234567890')
response = client.put(path=path, payload='gaoyanbin')
# response = client.get(path=path)
print response.pretty_print()
client.stop()