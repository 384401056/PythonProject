#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
from backend.core import request_handler
from backend import commons
from models import orm
import datetime
import json

class RegisterHandler(request_handler.BaseRquestHandler):
    pass


class SendCodeHandler(request_handler.BaseRquestHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self, *args, **kwargs):
        result = {'status':True, 'data':'', 'error':''} # 返回值格式

        user_email = self.get_argument('email')

        if user_email:

            sc = orm.Sendcode()
            sc.email = user_email
            sc.code = commons.random_code()
            sc.start_time = datetime.datetime.now() # 获取当前时间.

            session = orm.session()()
            session.add(sc) # 添加到数据库
            session.commit() # 提交
        else:
            result['error'] = '邮箱为空!'
            result['status'] = False

        self.write(json.dumps(result)) # 返回json数据

def main():
    pass


if __name__ == '__main__':
    main()
