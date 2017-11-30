#!/usr/bin/env python
# -*- coding:utf-8 -*-

from backend.core import request_handler

class IndexHandler(request_handler.BaseRquestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html', error_msg=None)


def main():
    pass


if __name__ == '__main__':
    main()
