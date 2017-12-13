#!/usr/bin/env python
# -*- coding utf-8 -*-

from coapthon.server.coap import CoAP
from exampleresources import *
# import requests

class MyResource(BasicResource):


    def render_POST(self, request):
        print 'post', request.payload
        # ret = requests.post('http://127.0.0.1:8080/coap', data={'payload': request.payload})
        # print ret.text
        self.payload = "111111"
        return super(MyResource, self).render_POST(request)


    def render_GET(self, request):
        print 'get', request.uri_path
        # ret = requests.get('http://127.0.0.1:8080/coap')
        # print ret.text
        self.payload = "111111"
        return super(MyResource, self).render_GET(request)

    def render_PUT(self, request):
        print 'put', request.payload
        self.payload = "111111"
        return super(MyResource, self).render_PUT(request)


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        # self.add_resource('', MyResource())
        self.add_resource('basic/', MyResource())
        self.add_resource('', MyResource())
        self.add_resource('storage/', Storage())
        self.add_resource('separate/', Separate())
        self.add_resource('long/', Long())
        self.add_resource('big/', Big())
        self.add_resource('void/', voidResource())
        self.add_resource('xml/', XMLResource())
        self.add_resource('encoding/', MultipleEncodingResource())
        self.add_resource('etag/', ETAGResource())
        self.add_resource('child/', Child())
        self.add_resource('advanced/', AdvancedResource())
        self.add_resource('advancedSeparate/', AdvancedResourceSeparate())
        print "CoAP Server start on " + host + ":" + str(port)
        # print self.root.dump()



    def receive_request(self, transaction):
        print 'request:', transaction.request
        # print transaction.request.payload
        # ret = requests.get('http://127.0.0.1:8080/coap',params=transaction.request.payload)
        # ret = requests.post('http://127.0.0.1:8080/coap', data={'payload': transaction.request.payload})
        # print ret
        super(CoAPServer, self).receive_request(transaction)

    def send_datagram(self, message):
        # import json
        # message.payload=json.dumps({'name':'gaoyanbin', 'status':'live'})
        message.payload="Hello Coap!"
        super(CoAPServer, self).send_datagram(message)


def main():
    server = CoAPServer("0.0.0.0", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print "Server Shutdown"
        server.close()
        print "Exiting..."

if __name__ == '__main__':
    main()