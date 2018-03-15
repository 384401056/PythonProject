#!/usr/bin/env python
# -*- coding utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import time
import hashlib

# 存储session信息的字典.一般放在radis中。
container = dict()


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):



        # 如果用户名正确
        if self.get_argument('u', None) in ['alex', 'gyb']:
            # 生成MD5码
            obj = hashlib.md5()
            md5_bytes = bytes(str(time.time()), encoding='utf-8')
            obj.update(md5_bytes)
            md5_str = obj.hexdigest()

            user_dict = dict()
            user_dict['name'] = self.get_argument('u')
            user_dict['is_login'] = True

            # 将用户信息保存到container中
            container[md5_str] = user_dict
            self.write(container)

            # 将生成的MD5k唯一标识写入客户端的cookeis中
            self.set_cookie('user_identity', md5_str)
            # self.write(bytes(self.get_cookie('user_identity'), encoding='utf-8'))
        else:
            self.write('用户名错误！')


class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        user_identity = self.get_cookie('user_identity',None)
        print(user_identity)
        user_info = container.get(user_identity, None) # 通过md5码获取container中的用户信息。
        print(user_info)
        if user_info is None:
            self.write('还没登录.')
        else:
            if user_info.get('is_login', None):
                self.write(user_info)
            else:
                self.write('还没登录.')



# class ShowContHandler(tornado.web.RequestHandler):
#     def get(self, *args, **kwargs):
#         self.write(container)

settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
    'cookie_secret': 'abcdefghijklmn',  # 设置签名的key
}

application = tornado.web.Application([
    (r'/index', IndexHandler),
    (r'/manager', ManagerHandler),
    # (r'/show', ShowContHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

































