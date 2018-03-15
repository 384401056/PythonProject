#!/usr/bin/env python
# -*- coding:utf-8 -*-
# python 2.7

from wsgiref.simple_server import make_server
import os

def index():
    return '<h1> Index </h1>'


def user():
    '''通过html文件来返回页面.'''
    with open(os.path.join('html', 'user.html'), 'r') as f:
        data = f.read()
    return data


def new():
    return '<h1> New </h1>'


# url与执行方法的对应字典
URLS = {
    '/index': index,
    '/user': user,
    '/new': new,
}


def RunServer(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = env['PATH_INFO']

    # 根据不同的url执行不同的方法.
    if url in URLS.keys():
        func = URLS[url]
        ret = func()
    else:
        ret = '<h1>404</h1>'
    return ret


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8000, RunServer)
    httpd.serve_forever()
