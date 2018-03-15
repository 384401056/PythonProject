#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coapthon.server.coap import CoAP
from exampleresources import *
from coapthon import defines
from coapthon.resources.resource import Resource
import logging
import logging.handlers
# import requests
import json

# LOG_FILE = 'coaplog.log'
# log = logging.getlog('coap')

logging.config.fileConfig("logging.conf")  # 采用配置文件
log = logging.getLogger('coap')

class MyResource(Resource):

    def render_POST(self, request):
        log.info('MyResource.render_POST:%s' % request.payload)
        self.payload = (1,'POST')
        return self

    def render_GET(self, request):
        log.info('MyResource.render_GET:%s' % request.payload)
        self.payload = (1,'GET')
        return self

    def render_PUT(self, request):
        log.info('MyResource.render_PUT:%s' % request.payload)
        self.payload = (1,'PUT')
        return self


class CoAPServer(CoAP):
    def __init__(self, host, port, multicast=False):
        CoAP.__init__(self, (host, port), multicast)
        self.add_resource('t/', MyResource(self))
        log.info("CoAP Server start on %s:%s" % (host, str(port)))

    def receive_request(self, transaction):
        log.info('-------------------------------receive_request----------------------------------')
        log.info('request: %s' % transaction.request)
        log.info('request token: %s' % transaction.request.token)
        log.info('request uri_path: %s' % transaction.request.uri_path)
        log.info('request payload: %s' % transaction.request.payload)
        super(CoAPServer, self).receive_request(transaction)

    def send_datagram(self, message):
        log.info('send_datagram: %s' % message)
        log.info('send_payload: %s' % message.payload)
        log.info('--------------------------------------end---------------------------------------')
        super(CoAPServer, self).send_datagram(message)


def init_log():
    """初始化日志"""
    fmt = '%(asctime)s - %(levelname)s : %(message)s'

    handler = logging.handlers.RotatingFileHandler('coaplog.log', maxBytes=1024 * 1024 * 100, backupCount=5)
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    log.addHandler(handler)  # 为log添加handler

    # 默认coap模块中已经有log了，所以屏幕的输出可以用他的。
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    log.addHandler(console)  # 为log添加handler


def main():
    # init_log()
    server = CoAPServer("127.0.0.1", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        log.info("Server Shutdown")
        server.close()
        log.info("Exiting...")


if __name__ == '__main__':
    main()
