#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import time
import config
import memcache
import json

session_id = 'user_identity' # cookie中随机字符串的key
container = dict()
mem_conn = memcache.Client(['192.168.20.130:11211'], debug=True)


class SessionFactory:
    @staticmethod
    def get_session_obj(handler):
        obj = MemcachedSession(handler)
        return obj


class CacheSession:

    def __init__(self, handler):
        self.handler = handler
        self.random_str = None

    def __setitem__(self, key, value):
        return self.set_value(key, value)

    def __getitem__(self, item):
        return self.get_value(item)

    def set_value(self, key, value):
        # 第一次注册时，虽然设置了cookies，但是此时get_cookie是取不得值的。
        # 所以要用self.random_str来判断.
        if not self.random_str:
            # 从客户端获取随机字符串
            client_random_str = self.handler.get_cookie(session_id, None)

            # 如果客户端存在，并且服务器内存中也存在。
            if client_random_str and (client_random_str in container.keys()):
                self.random_str = client_random_str
            else:
                self.random_str = create_session_id()  # 生成随机字符串.
                container[self.random_str] = {}  # 清空服务端的随机字符串字典信息。
        # 设置用户信息
        container[self.random_str][key] = value

        # 将生成的随机字符串唯一标识写入客户端的cookeis中
        # 此处写入是为了以后更新失效时间。
        self.handler.set_cookie(session_id, self.random_str)

    def get_value(self, key):
        # 从客户端获取随机字符串
        client_random_str = self.handler.get_cookie(session_id, None)

        # 如果客户端存在，并且服务器内存中也存在。
        if client_random_str and (client_random_str in container):
            # 通过md5码获取container中的用户信息。
            user_info = container.get(client_random_str, None)
            return user_info.get(key, None)
        else:
            return None


# class CacheSessionBack:
#     session_id = 'user_identity'
#
#     def __init__(self, handler):
#         self.handler = handler
#         self.random_str = None
#
#     def __setitem__(self, key, value):
#         """将原来的set_value方法写在 __setitem__中后，就可以 seesion['key'] = value 这样来使用session对象了."""
#         self.set_value(key, value)
#
#     def __getitem__(self, item):
#         """将原来的get_value方法写在 __getitem__中后，就可以 seesion['key'] 这样来使用session对象了."""
#         return self.get_value(item)
#
#     def __get_random_str(self):
#         """生成MD5码"""
#         obj = hashlib.md5()
#         md5_bytes = bytes(str(time.time()), encoding='utf-8')
#         obj.update(md5_bytes)
#         random_str = obj.hexdigest()
#         return random_str
#
#     def set_value(self, key, value):
#         if not self.random_str:
#             random_str = self.handler.get_cookie(CacheSession.session_id, None)
#             # 如果客户端没有随机MD5码
#             if not random_str:
#                 # 生成md5码
#                 random_str = self.__get_random_str()
#                 # 则创建新的md5码和用户信息空字典。
#                 container[random_str] = {}
#             else:
#                 # 如果客户端有md5,但服务器端由于重启了，没有md5了.则创建新的md5码和用户信息空字典。
#                 if not (random_str in container.keys()):
#                     # 生成md5码
#                     random_str = self.__get_random_str()
#                     container[random_str] = {}
#                 else:
#                     # 如果两边都有md5,则什么也不用做。
#                     pass
#             self.random_str = random_str
#         # 设置用户信息
#         container[self.random_str][key] = value
#
#         # 将生成的MD5k唯一标识写入客户端的cookeis中
#         # 此处写入是为了以后更新失效时间。
#         self.handler.set_cookie(CacheSession.session_id, self.random_str)
#
#     def get_value(self, key):
#         random_str = self.handler.get_cookie(CacheSession.session_id, None)
#
#         # 如果没有md5,则返回None
#         if not random_str:
#             return None
#
#         user_info = container.get(random_str, None)  # 通过md5码获取container中的用户信息。
#         # 如果服务器端没有user_info
#         if not user_info:
#             return None
#         # return user_info.get(key, None)


class MemcachedSession:
    """使用memcached来存储session信息"""
    def __init__(self, handler):
        self.handler = handler
        self.random_str = None

    def __setitem__(self, key, value):
        return self.set_value(key, value)

    def __getitem__(self, item):
        return self.get_value(item)

    def set_value(self, key, value):
        # 第一次注册时，虽然设置了cookies，但是此时get_cookie是取不得值的。
        # 所以要用self.random_str来判断.
        if not self.random_str:
            # 从客户端获取随机字符串
            client_random_str = self.handler.get_cookie(session_id, None)

            # 如果客户端存在，并且服务器内存中也存在。
            if client_random_str and mem_conn.get(client_random_str):
                self.random_str = client_random_str
            else:
                self.random_str = create_session_id()  # 生成随机字符串.
                container[self.random_str] = {}
                mem_conn.set(self.random_str, json.dumps({}), config.SESSION_EXPIRES)  # 清空memcached服务端的随机字符串字典信息。

        # 设置用户信息
        container[self.random_str][key] = value
        mem_conn.set(self.random_str, json.dumps(container[self.random_str]), config.SESSION_EXPIRES)# 将json数据存入memcahed中。

        # 将生成的随机字符串唯一标识写入客户端的cookeis中
        # 此处写入是为了以后更新失效时间。
        self.handler.set_cookie(session_id, self.random_str)

    def get_value(self, key):
        # 从客户端获取随机字符串
        client_random_str = self.handler.get_cookie(session_id, None)

        # 如果客户端存在，并且服务器内存中也存在。
        if client_random_str and mem_conn.get(client_random_str):
            user_info = json.loads(mem_conn.get(client_random_str)) # 从memcached中取出数据,转为dict对象
            return user_info.get(key, None)
        else:
            return None


class RedisSession:
    def __init__(self, handler):
        pass


def create_session_id():
    """生成随机字符串"""
    obj = hashlib.md5()
    md5_bytes = bytes(str(time.time()), encoding='utf-8')
    obj.update(md5_bytes)
    random_str = obj.hexdigest()
    return random_str


def main():
    pass


if __name__ == '__main__':
    main()
