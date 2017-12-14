#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coapthon.server.coap import CoAP
from exampleresources import *
from coapthon import defines
import logging
import logging.handlers
# import requests
import json

# LOG_FILE = 'coaplog.log'
# log = logging.getlog('coap')

logging.config.fileConfig("logging.conf")  # 采用配置文件
log = logging.getLogger('coap')

class MyResource(BasicResource):


    def render_POST(self, request):
        log.info('post:%s' % request.payload)
        # ret = requests.post('http://127.0.0.1:8080/coap', data={'payload': request.payload})
        # log.info(ret.text
        self.payload = "BasicResource post"
        return super(MyResource, self).render_POST(request)


    def render_GET(self, request):
        # log.info('get', request.uri_path
        # ret = requests.get('http://127.0.0.1:8080/coap')
        # log.info(ret.text
        self.payload = "BasicResource get"
        return super(MyResource, self).render_GET(request)

    def render_PUT(self, request):
        # log.info('put', request.payload
        self.payload = "BasicResource put"
        return super(MyResource, self).render_PUT(request)


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('basic/', MyResource())
        # self.add_resource('basic/', MyResource())
        # self.add_resource('storage/', Storage())
        # self.add_resource('separate/', Separate())
        # self.add_resource('long/', Long())
        # self.add_resource('big/', Big())
        # self.add_resource('void/', voidResource())
        # self.add_resource('xml/', XMLResource())
        # self.add_resource('encoding/', MultipleEncodingResource())
        # self.add_resource('etag/', ETAGResource())
        # self.add_resource('child/', Child())
        # self.add_resource('advanced/', AdvancedResource())
        # self.add_resource('advancedSeparate/', AdvancedResourceSeparate())
        log.info("CoAP Server start on %s:%s" % (host ,str(port)))
        # log.info(self.root.dump()



    def receive_request(self, transaction):
        log.info('-------------------------------start receive----------------------------------')
        log.info('request: %s' % transaction.request)
        # log.info('request type:', transaction.request.type
        log.info('request type: %s' % list(defines.Types.keys())[list(defines.Types.values()).index(transaction.request.type)])
        """
            'CON': 0,
            'NON': 1,
            'ACK': 2,
            'RST': 3,
            'None': None
        """
        log.info('request mid: %s' %transaction.request.mid)
        log.info('request token: %s' % transaction.request.token)
        log.info('request destination: %s' % json.dumps(transaction.request.destination))
        log.info('request source: %s' % json.dumps(transaction.request.source))
        log.info('request uri_path: %s' % transaction.request.uri_path)
        log.info('request payload: %s' % transaction.request.payload)


        # 将请求发往Tornado服务器
        # ret = requests.get('http://127.0.0.1:8080/coap',params=transaction.request.payload)
        # ret = requests.post('http://127.0.0.1:8080/coap', data={'payload': transaction.request.payload})

        super(CoAPServer, self).receive_request(transaction)

    def send_datagram(self, message):

        log.info('message:%s' % message)
        # log.info('request type:', message.type
        log.info('message type: %s' % list(defines.Types.keys())[list(defines.Types.values()).index(message.type)])
        """
            'CON': 0,
            'NON': 1,
            'ACK': 2,
            'RST': 3,
            'None': None
        """
        log.info('message mid: %s' % message.mid)
        log.info('message token: %s' % message.token)
        log.info('message destination: %r' % json.dumps(message.destination))
        log.info('message source: %s' % json.dumps(message.source))
        log.info('message payload: %s' % message.payload)
        log.info('----------------------------------send over---------------------------------------')

        if not message.payload:
            message.payload="Hello Coap!"
        super(CoAPServer, self).send_datagram(message)


def init_log():
    """初始化日志"""
    fmt = '%(asctime)s - %(levelname)s : %(message)s'

    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024 * 100, backupCount=5)
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
    server = CoAPServer("0.0.0.0", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        log.info("Server Shutdown")
        server.close()
        log.info("Exiting...")



if __name__ == '__main__':
    main()