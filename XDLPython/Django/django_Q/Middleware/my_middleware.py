#!/usr/bin/env python
# -*- coding utf-8 -*-

"""对照settings文件中的中间件，编写自己的中间件"""
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware1(MiddlewareMixin):

    def __init__(self, get_response=None):
        super().__init__(get_response)

    # 接收请求的方法，如果在此方法中 return HttpResponse(''),则请求不再往下传递。
    # 而是直接跳至Urls之前的中间件process_response方法中去。
    def process_request(self, request):
        print('===TestMiddleware11111===')
        # return HttpResponse("TestMiddleware1")

    # 在view执行前执行的方法.
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("====process_view1111111======")

    # 当view返回的对象中有render方法，才会执行的方法.
    def process_template_response(self,request,response):
        print('=====process_template_response11111========')

    # 当view出异常时，会被执行的方法。
    def process_exception(self, request, exception):
        print('====process_exception1111111===')

    # 接收返回数据的方法。
    def process_response(self, request, response):
        print('===response TestMiddleware11111===')
        return response


class TestMiddleware2(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)

    def process_request(self, request):
        print('===TestMiddleware22222===')
        # return render(request, 'Middleware/index.html') # 中间件在接收请求的方法中，直接返回了。

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("====process_view222222======")


    def process_template_response(self,request,response):
        print('=====process_template_response2222========')


    def process_exception(self, request, exception):
        print('====process_exception22222===')

    def process_response(self, request, response):
        print('===response TestMiddleware22222===')
        return response


class TestMiddleware3(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)

    def process_request(self, request):
        print('===TestMiddleware3333333===')


    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("====process_view333333======")

    def process_template_response(self,request,response):
        print('=====process_template_response3333========')

    def process_exception(self, request, exception):
        print('====process_exception333333===')

    def process_response(self, request, response):
        print('===response TestMiddleware3333333===')
        return response