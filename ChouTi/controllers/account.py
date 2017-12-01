#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
from backend.core import request_handler
from backend.forms import forms
from backend import commons
from models import orm
import datetime
import json
from sqlalchemy import *

class RegisterHandler(request_handler.BaseRquestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        result = {'status': True, 'data': '', 'error': ''}  # 返回值格式

        checkcode = self.get_argument('checkcode')
        email = self.get_argument('email')

        obj = forms.RegForm()
        is_valid, success_dict, error_msg = obj.check_valid(self)

        # 如果表单验证通过
        if is_valid:
            conn = orm.session()
            # 查询出，code与email对应的数据
            # session.query(User).filter(and_(User.name.like("user%"), User.fullname.like("first%"))).all()
            ret = conn.query(orm.Sendcode).filter(
                and_(orm.Sendcode.code == checkcode, orm.Sendcode.email== email)
            ).first()
            # 如果有数据则，添加用户到userinfo表.
            if ret:
                user = orm.UserInfo()
                user.username = self.get_argument('reg_name')
                user.email = self.get_argument('email')
                user.password = self.get_argument('reg_pwd')
                user.ctime = datetime.datetime.now()
                user.status = 1

                conn.add(user)
                conn.commit()  # 提交
                conn.close()

                print(self.session)
                # 将session信息写入cookies中
                self.session['is_login'] = True
                self.session['reg_name'] = self.get_argument('reg_name')
                self.session['email'] = self.get_argument('email')

            else:
                result['status'] = False
                result['error'] = '邮箱验证码错误!'

            self.write(json.dumps(result))

        else:
            self.render('error.html', error_msg=error_msg)

class LoginHandler(request_handler.BaseRquestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
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

            conn = orm.session()
            conn.add(sc) # 添加到数据库
            conn.commit() # 提交
            print(sc.code)
            conn.close()
        else:
            result['error'] = '邮箱为空!'
            result['status'] = False

        self.write(json.dumps(result)) # 返回json数据

def main():
    pass


if __name__ == '__main__':
    main()
