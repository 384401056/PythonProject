#!/usr/bin/env python
# -*- coding utf-8 -*-

# 注意，作为 ui_methods 的函数，第一个参数要是self,就是Mainhandler的对象
def myfunc(self, arg):
    return '这是一个 ui_methods 的函数调用... 用户列表数：%d' % len(arg)