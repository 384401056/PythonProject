#!/usr/bin/env python
# -*- coding:utf-8 -*-

from backend.core import request_handler

class IndexHandler(request_handler.BaseRquestHandler):
    def get(self, *args, **kwargs):
        userinfo = {}
        if self.session['is_login']:
            userinfo['is_login'] = self.session['is_login']
            userinfo['reg_name'] = self.session['reg_name']
            userinfo['email'] = self.session['email']

            self.render('index.html', error_msg=None, userinfo=userinfo)
        else:
            self.render('index.html', error_msg = None, userinfo = None)
            self.write()
def main():
    pass


if __name__ == '__main__':
    main()
