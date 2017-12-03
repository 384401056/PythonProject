#!/usr/bin/env python
# -*- coding:utf-8 -*-

from backend.core import request_handler
from models import orm
from sqlalchemy import *
import json


class IndexHandler(request_handler.BaseRquestHandler):
    def get(self, *args, **kwargs):

        # try:
        #     news_type = self.get_argument('newstype')
        # except Exception as ex:
        #     news_type = 0
        #     print(ex)

        userinfo = {}
        # 获取新闻数据
        conn = orm.session()

        news_list = conn.query(orm.News, orm.UserInfo).filter(
            orm.News.user_info_id == orm.UserInfo.nid
        ).all()

        # if news_type:
        #     news_list = conn.query(orm.News, orm.UserInfo).filter(
        #         and_(orm.News.user_info_id == orm.UserInfo.nid, orm.News.news_type_id == news_type)
        #     ).all()
        # else:
        #     news_list = conn.query(orm.News, orm.UserInfo).filter(
        #         orm.News.user_info_id == orm.UserInfo.nid
        #     ).all()

        # print(json.loads(ret))
        if self.session['is_login']:
            userinfo['is_login'] = self.session['is_login']
            userinfo['reg_name'] = self.session['reg_name']
            userinfo['email'] = self.session['email']
            self.render('index.html', error_msg=None, userinfo=userinfo, news=news_list)
        else:
            self.render('index.html', error_msg=None, userinfo=None, news=news_list)


def main():
    pass


if __name__ == '__main__':
    main()
