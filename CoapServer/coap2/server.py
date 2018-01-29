#!/usr/bin/env python
# -*- coding: utf-8 -*-


from coapthon.server.coap import CoAP
from examplersources import *
from coapthon import defines
from coapthon.messages.response import Response
import logging
import logging.handlers
import json

logging.config.fileConfig("logging.conf")  # 采用配置文件
log = logging.getLogger('coap')


class MyResource(Resource):
    def __init__(self, name="Advanced"):
        super(MyResource, self).__init__(name)
        self.payload = "This response from Gaoyanbin By Get"

    def render_GET_advanced(self, request, response):
        self.printInfo(request)
        response.payload = self.payload
        response.max_age = 20
        response.code = defines.Codes.CONTENT.number
        return self, response

    def render_POST_advanced(self, request, response):
        self.printInfo(request)
        self.payload = request.payload
        assert (isinstance(response, Response))
        response.payload = "This response from Gaoyanbin By POST"
        response.code = defines.Codes.CREATED.number
        return self, response

    def render_PUT_advanced(self, request, response):
        self.printInfo(request)
        self.payload = request.payload
        assert (isinstance(response, Response))
        response.payload = "This response from Gaoyanbin By PUT"
        response.code = defines.Codes.CHANGED.number
        return self, response

    def printInfo(self,request):
        log.info('===========================receive_request==============================')
        log.info('request: %s' % request)
        log.info('request type: %s' % list(defines.Types.keys())[
            list(defines.Types.values()).index(request.type)])
        """
            'CON': 0,
            'NON': 1,
            'ACK': 2,
            'RST': 3,
            'None': None
        """
        log.info('request mid: %s' % request.mid)
        log.info('request token: %s' % request.token)
        log.info('request destination: %s' % json.dumps(request.destination))
        log.info('request source: %s' % json.dumps(request.source))
        log.info('request uri_path: %s' % request.uri_path)
        log.info('request payload Hex: %s' % ' '.join(hex(x) for x in bytearray(request.payload.encode("utf8"))))
        log.info('request payload ascii: [%s]' % ' '.join(str(x) for x in bytearray(request.payload.encode("utf8"))))
        log.info('request payload String: %s' % str(bytearray(request.payload.encode("utf8"))))


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('t/', MyResource())

    def receive_request(self, transaction):
        super(CoAPServer, self).receive_request(transaction)

    def send_datagram(self, message):
        log.info('---------------------------send_datagram---------------------------------')
        log.info('send_datagram: %s' % message)
        log.info('send_payload: %s' % message.payload)
        log.info('=================================end======================================')
        super(CoAPServer, self).send_datagram(message)


def main():
    server = CoAPServer("0.0.0.0", 5683)
    try:
        log.info("Server listen...")
        server.listen(10)
    except KeyboardInterrupt:
        log.info("Server Shutdown")
        server.close()
        log.info("Exiting...")


if __name__ == '__main__':
    main()
