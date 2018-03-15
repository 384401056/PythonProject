#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
from backend.core import request_handler
from backend import commons


class RegisterHandler(request_handler.BaseRquestHandler):
    pass


class SendCodeHandler(request_handler.BaseRquestHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self, *args, **kwargs):
        print(self.get_argument('email'))
        print(commons.random_code)


def main():
    pass


if __name__ == '__main__':
    main()
