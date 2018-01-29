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
        self.payload = "This response from Gaoyanbin"

    def render_GET_advanced(self, request, response):
        response.payload = self.payload
        response.max_age = 20
        response.code = defines.Codes.CONTENT.number
        return self, response

    def render_POST_advanced(self, request, response):
        self.payload = request.payload
        assert (isinstance(response, Response))
        response.payload = "This response from Gaoyanbin"
        response.code = defines.Codes.CREATED.number
        return self, response

    def render_PUT_advanced(self, request, response):
        self.payload = request.payload
        assert (isinstance(response, Response))
        response.payload = "This response from Gaoyanbin"
        response.code = defines.Codes.CHANGED.number
        return self, response


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('t/', MyResource())

    def receive_request(self, transaction):
        log.info('================================start receive=================================')
        log.info('request: %s' % transaction.request)
        log.info('request type: %s' % list(defines.Types.keys())[
            list(defines.Types.values()).index(transaction.request.type)])
        """
            'CON': 0,
            'NON': 1,
            'ACK': 2,
            'RST': 3,
            'None': None
        """
        log.info('request mid: %s' % transaction.request.mid)
        log.info('request token: %s' % transaction.request.token)
        log.info('request destination: %s' % json.dumps(transaction.request.destination))
        log.info('request source: %s' % json.dumps(transaction.request.source))
        log.info('request uri_path: %s' % transaction.request.uri_path)
        log.info('request payload: %s' % transaction.request.payload)
        log.info('---------------------------------end------------------------------------------')
        super(CoAPServer, self).receive_request(transaction)


def main():
    server = CoAPServer("127.0.0.1", 5683)
    try:
        log.info("Server listen...")
        server.listen(10)
    except KeyboardInterrupt:
        log.info("Server Shutdown")
        server.close()
        log.info("Exiting...")


if __name__ == '__main__':
    main()
