#!/usr/bin/env python
# -*- coding utf-8 -*-

from coapthon.client.helperclient import HelperClient
from coapthon.messages.message import Message

host = "118.190.43.87"
# host = "10.88.20.21"
port = 5683
path =""



# def client_callback_observe(response):  # pragma: no cover
#     logger.info( 'version:', response.version
#     logger.info( 'type:', response.type
#     logger.info( 'mid:', response.mid
#     logger.info( 'token:', response.token
#     logger.info( 'options:', response.options
#     print 'destination:', response.destination
#     print 'source:', response.source
#     print 'payload:', response.payload


def client_callback_observe(response):
    print 'version:',response.version
    print 'type:', response.type
    print 'mid:', response.mid
    print 'token:', response.token
    print 'options:', response.options
    print 'destination:', response.destination
    print 'source:', response.source
    print 'payload:', response.payload
    client.close()

client = HelperClient(server=(host, port))
response = client.put(path=path, payload='222222', callback=client_callback_observe)
# response = client.observe(path,callback=client_callback_observe)

# response = client.get(path=path+'?22222')
# response = client.post(path=path, payload='22222')
# print response.pretty_print()
# print response.line_print()

def get_request():
    response = client.get(path=path)
    print 'version:',response.version
    print 'type:', response.type
    print 'mid:', response.mid
    print 'token:', response.token
    print 'options:', response.options
    print 'destination:', response.destination
    print 'source:', response.source
    print 'payload:', response.payload
    client.stop()

# get_request()