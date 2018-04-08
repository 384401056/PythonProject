#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import json
import RedisConn
import hashlib
import random
import time


class BaseHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


class Login(BaseHandler):
    """用户登陆后在redis中生成token"""
    def post(self, *args, **kwargs):
        ret = {}
        user_dict = {}
        username = self.get_argument('name', None)
        pwd = self.get_argument('pwd', None)

        if username == 'admin' and pwd == '123456':
            self.conn = RedisConn.RedisConn().getConn()
            user_dict['userid'] = random.randint(1, 9999)
            user_dict['token'] = getMd5()
            self.conn.set(user_dict['userid'], json.dumps(user_dict))
            ret['status'] = 1
            ret['data'] = user_dict
        else:
            ret['status'] = 0
            ret['error'] = '用户名密码错误'
        self.write(json.dumps(ret))


class UserInfo(BaseHandler):
    """使用URL签名信息+时间来提高接口的安全性"""
    def get(self, *args, **kwargs):
        ret = {}
        url = '/user/info' # UserInfo类的url
        uerId = self.get_argument('userId')
        client_sign = self.get_argument('sign')
        timestamp = self.get_argument('timestamp')

        # 如果URL中带过来的timestamp
        if time.time() - float(timestamp) > 30:
            ret['status'] = 0
            ret['error'] = '认证超时'
        else:
            # 通过userId查找对应的token
            self.conn = RedisConn.RedisConn().getConn()
            st = json.loads(self.conn.get(uerId))
            token = st['token']
            md5str = url + 'token=' + str(token)  # 将url和token组合后生成一个md5码
            sign = getMd5ByStr(md5str) # 生成URL签名信息

            if client_sign == sign:
                ret['status'] = 1
            else:
                ret['status'] = 0
                ret['error'] = '认证失败'

        self.write(json.dumps(ret))


# class AddUser(BaseHandler):
#     def post(self, *args, **kwargs):
#         ret = {}
#         user_dict = {}
#         username = self.get_argument('name', None)
#         pwd = self.get_argument('pwd', None)
#
#         if user_dict is not None and pwd is not None:
#             userid = random.randint(1, 9999)
#             user_dict['username'] = username
#             user_dict['pwd'] = pwd
#             self.conn = RedisConn.RedisConn(db=0).getConn()
#             self.conn.set(userid, user_dict)
#             ret['status'] = 1
#         else:
#             ret['status'] = 0
#             ret['error'] = '用户名密码不能为空'
#
#         self.write(json.dumps(ret))

def getMd5():
    # 生成MD5码
    obj = hashlib.md5()
    md5_bytes = bytes(str(time.time()), encoding='utf-8')
    obj.update(md5_bytes)
    md5_str = obj.hexdigest()
    return md5_str

def getMd5ByStr(s):
    # 生成MD5码
    obj = hashlib.md5()
    md5_bytes = bytes(str(s), encoding='utf-8')
    obj.update(md5_bytes)
    md5_str = obj.hexdigest()
    return md5_str