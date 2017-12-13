#!/usr/bin/env python
# -*- coding utf-8 -*-

from coapthon.client.helperclient import HelperClient
from coapthon.messages.message import Message

host = "118.190.43.87"
# host = "10.88.20.21"
port = 5683
path =""



# def client_callback_observe(response):  # pragma: no cover
#     print 'version:', response.version
#     print 'type:', response.type
#     print 'mid:', response.mid
#     print 'token:', response.token
#     print 'options:', response.options
#     print 'destination:', response.destination
#     print 'source:', response.source
#     print 'payload:', response.payload


client = HelperClient(server=(host, port))
# response = client.observe(path,callback=client_callback_observe)
response = client.get(path=path)
# response = client.get(path=path+'?22222')
# response = client.post(path=path, payload='22222')
# print response.pretty_print()
# print response.line_print()
print 'version:',response.version
print 'type:', response.type
print 'mid:', response.mid
print 'token:', response.token
print 'options:', response.options
print 'destination:', response.destination
print 'source:', response.source
print 'payload:', response.payload
client.stop()