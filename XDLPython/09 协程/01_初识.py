#!/usr/bin/env python
# -*- coding utf-8 -*-

from greenlet import greenlet

# def f1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
#
# def f2():
#     print(56)
#     gr1.switch()
#     print(78)
#
#
# gr1 = greenlet(f1)
# gr2 = greenlet(f2)
# gr1.switch()


# import gevent
#
# def foo():
#     print('Running in foo')
#     gevent.sleep(0)
#     print('Explicit context switch to foo again')
#
#
# def bar():
#     print('Explicit context to bar')
#     gevent.sleep(0)
#     print('Implicit context switch back to bar')
#
# def three():
#     print('Explicit context to three')
#     gevent.sleep(0)
#     print('Implicit context switch back to ？')
#
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
#     gevent.spawn(three),
# ])


from gevent import monkey; monkey.patch_all()
import gevent
import requests
import time

def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))

start_time = time.time()
gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'http://www.163.com/'),
        gevent.spawn(f, 'http://www.qq.com/'),
        gevent.spawn(f, 'https://github.com/'),
])
end_time = time.time()
print(end_time-start_time)

# 不使用协程的情况。
# start_time = time.time()
# f('https://www.python.org/')
# f('http://www.163.com/')
# f('http://www.qq.com/')
# f('https://github.com/')
# end_time = time.time()
# print(end_time-start_time)




