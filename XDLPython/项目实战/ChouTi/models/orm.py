#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

# 创建ORM基类
Base = declarative_base()

class userInfo(Base):
    __tablename__ = 'userinfo'

    nid = Column(Integer, primary_key=True, autoincrement=True)  # id
    username = Column(String(32))  # 用户名
    password = Column(String(32))  # 密码
    email = Column(String(32))  # 邮箱
    ctime = Column(TIMESTAMP)  # 创建时间

    __table_args__ = (
        Index('ix_user_pwd', 'username', 'password'),  # 创建用户名和密码的索引
        Index('ix_email_pwd', 'email', 'password'),  # 创建邮箱和密码的索引
    )


class newstype(Base):
    __tablename__ = 'newstype'

    nid = Column(Integer, primary_key=True, autoincrement=True)  # id
    caption = Column(String(32))


class news(Base):
    __tablename__ = 'news'

    nid = Column(Integer, primary_key=True, autoincrement=True)  # id
    user_info_id = Column(Integer, ForeignKey('userinfo.nid'))  # 用户ID,外键 userinfo.nid
    news_type_id = Column(Integer, ForeignKey('newstype.nid'))  # 新闻类型id, 外键 newstype.nid
    ctime = Column(TIMESTAMP)  # 创建时间
    title = Column(String(32))
    url = Column(String(128))
    content = Column(String(300))


class favor(Base):
    __tablename__ = 'favor'

    nid = Column(Integer, primary_key=True, autoincrement=True)  # id
    user_info_id = Column(Integer, ForeignKey('userinfo.nid'))  # 用户ID,外键 userinfo.nid
    news_id = Column(Integer, ForeignKey('news.nid'))
    ctime = Column(TIMESTAMP)  # 创建时间

    # 联合唯一的约束
    __table_args__ = (
        UniqueConstraint('user_info_id', 'news_id', name='uix_uid_nid'),
    )


class comment(Base):
    __tablename__ = 'comment'

    nid = Column(Integer, primary_key=True, autoincrement=True)  # id
    user_info_id = Column(Integer, ForeignKey('userinfo.nid'))  # 用户ID,外键 userinfo.nid
    news_id = Column(Integer, ForeignKey('news.nid'))
    reply_id = Column(Integer, ForeignKey('comment.nid'), nullable=True, default=None)
    up = Column(Integer)  # 顶
    down = Column(Integer)  # 踩
    ctime = Column(TIMESTAMP)  # 创建时间
    device = Column(String(32))  # 发帖设备
    content = Column(String(200))  # 评论内容


def main():
    ENGINE = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/chouti?charset=utf8")  # echo为显示打印sql语句
    # 创建所有表结构
    Base.metadata.create_all(ENGINE)

if __name__ == '__main__':
    main()
