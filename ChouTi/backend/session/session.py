#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import time

container = dict()

class SessionFactory:
    @staticmethod
    def get_session_obj(handler):
        obj = CacheSession(handler)
        return obj

class CacheSession:

    def __init__(self, handler):
        self.handler = handler
        self.md5_str = None


    '''将原来的set_value方法写在 __setitem__中后，就可以 seesion['key'] = value 这样来使用session对象了.'''
    def __setitem__(self, key, value):
        self.set_value(key, value)

    '''将原来的get_value方法写在 __getitem__中后，就可以 seesion['key'] 这样来使用session对象了.'''
    def __getitem__(self, item):
        return self.get_value(item)

    '''生成MD5码'''
    def __get_md5_str(self):
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

class RedisSession:
    def __init__(self, handler):
        pass

class MemcachedSession:
    def __init__(self, handler):
        pass


def main():
    pass


if __name__ == '__main__':
    main()