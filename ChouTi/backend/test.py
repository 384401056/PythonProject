#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import orm
from sqlalchemy import *

def main():
    # 获取新闻数据
    conn = orm.session()
    news_list = conn.query(orm.News, orm.UserInfo).filter(
        and_(orm.News.user_info_id == orm.UserInfo.nid, orm.News.news_type_id==1)
    ).all()

    for item in news_list:
        print(item[0].title, item[1].username)


if __name__ == '__main__':
    main()