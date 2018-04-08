#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time

def getMd5ByStr(s):
    # 生成MD5码
    obj = hashlib.md5()
    md5_bytes = bytes(str(s), encoding='utf-8')
    obj.update(md5_bytes)
    md5_str = obj.hexdigest()
    return md5_str


def URLDecodeRequest():
    userId = 1661
    url = '/user/info'
    token = '036a2cefde197f9f5b60035bd71a1889'
    md5str = url + 'token=' + token
    print(md5str)
    timestamp = time.time()
    print(
        "生成调用的URL:" + url + '?userId=' + str(userId) + '&timestamp=' + str(timestamp) + '&sign=' + getMd5ByStr(md5str))


def AESDecodeRequest():
    userId = 1661
    url = '/user/info'
    token = '036a2cefde197f9f5b60035bd71a1889'
    md5str = url + 'token=' + token
    print(md5str)
    timestamp = time.time()
    print(
        "生成调用的URL:" + url + '?userId=' + str(userId) + '&timestamp=' + str(timestamp) + '&sign=' + getMd5ByStr(md5str))

if __name__ == '__main__':
    URLDecodeRequest()