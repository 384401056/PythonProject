#!/usr/bin/env python
# -*- coding utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import time
import hashlib

# 存储session信息的字典.一般放在radis中。
container = dict()

class Session:

    def __init__(self, handler):
        self.handler = handler
        self.md5_str = None


    def __get_md5_str(self):
        '''生成MD5码'''
        obj = hashlib.md5()
        md5_bytes = bytes(str(time.time()), encoding='utf-8')
        obj.update(md5_bytes)
        md5_str = obj.hexdigest()
        return md5_str


    def set_value(self, key, value):

        if not self.md5_str:
            md5_str = self.handler.get_cookie('user_identity', None)
            # 如果客户端没有随机MD5码
            if not md5_str:
                # 生成md5码
                md5_str = self.__get_md5_str()
                # 则创建新的md5码和用户信息空字典。
                container[md5_str] = {}
            else:
                # 如果客户端有md5,但服务器端由于重启了，没有md5了.则创建新的md5码和用户信息空字典。
                if not (md5_str in container.keys()):
                    # 生成md5码
                    md5_str = self.__get_md5_str()
                    container[md5_str] = {}
                else:
                    # 如果两边都有md5,则什么也不用做。
                    pass
            self.md5_str = md5_str
        # 设置用户信息
        container[self.md5_str][key] = value

        # 将生成的MD5k唯一标识写入客户端的cookeis中
        # 此处写入是为了以后更新失效时间。
        self.handler.set_cookie('user_identity', self.md5_str)


    def get_value(self, key):
        md5_str = self.handler.get_cookie('user_identity',None)

        # 如果没有md5,则返回None
        if not md5_str:
            return None

        user_info = container.get(md5_str, None) # 通过md5码获取container中的用户信息。
        # 如果服务器端没有user_info
        if not user_info:
            return None

        return user_info.get(key, None)



class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        # 如果用户名正确
        if self.get_argument('u', None) in ['alex', 'gyb']:
            session = Session(self)
            session.set_value('is_login', True)
            session.set_value('name', self.get_argument('u'))
            self.write(container)
        else:
            self.write('用户名错误！')


class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        session = Session(self)
        if session.get_value('is_login'):
            is_login = str(session.get_value('is_login'))
            name = str(session.get_value('name'))
            self.write(bytes('is_login: %s,  name: %s' % (is_login, name), encoding='utf-8'))
        else:
            self.write('还没登录.')



settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
    'cookie_secret': 'abcdefghijklmn',  # 设置签名的key
}

application = tornado.web.Application([
    (r'/index', IndexHandler),
    (r'/manager', ManagerHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

































