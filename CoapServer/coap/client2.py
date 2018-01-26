#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coapthon.client.helperclient import HelperClient

host = "118.190.43.87"
port = 5683
path ="t/r"

client = HelperClient(server=(host, port))
# response = client.post(path=path, payload='Hello Coap Server!')
# response = client.put(path=path, payload='gaoyanbin')
response = client.get(path=path)
print (response.pretty_print())
client.stop()