#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



ENGINE = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/chouti?charset=utf8")  # echo为显示打印sql语句

# 创建ORM基类
Base = declarative_base()


class Sendcode(Base):
    """验证码记录表"""
    __tablename__ = 'sendcode'

    nid = Column(Integer, primary_key=True, autoincrement=True)  # id
    email = Column(String(32)) # 邮箱名称
    start_time =  Column(TIMESTAMP)  # 开始时间
    code = Column(String(6))
    # status = Column(Integer) # 未用



class UserInfo(Base):
    """用户信息表"""
    __tablename__ = 'userinfo'

    nid = Column(Integer, primary_key=True, autoincrement=True)  # id
    username = Column(String(32))  # 用户名
    password = Column(String(32))  # 密码
    email = Column(String(32))  # 邮箱
    ctime = Column(TIMESTAMP)  # 创建时间
    status = Column(Integer) # 用户状态

    __table_args__ = (
        Index('ix_user_pwd', 'username', 'password'),  # 创建用户名和密码的索引
        Index('ix_email_pwd', 'email', 'password'),  # 创建邮箱和密码的索引
    )


class NewsType(Base):
    """新闻类型表"""
    __tablename__ = 'newstype'

    nid = Column(Integer, primary_key=True, autoincrement=True)  # id
    caption = Column(String(32))


class News(Base):
    """新闻内容表"""
    __tablename__ = 'news'

    nid = Column(Integer, primary_key=True, autoincrement=True)  # id
    user_info_id = Column(Integer, ForeignKey('userinfo.nid'))  # 用户ID,外键 userinfo.nid
    news_type_id = Column(Integer, ForeignKey('newstype.nid'))  # 新闻类型id, 外键 newstype.nid
    ctime = Column(TIMESTAMP)  # 创建时间
    title = Column(String(32))
    url = Column(String(128))
    content = Column(String(300))


class Favor(Base):
    """点赞表"""
    __tablename__ = 'favor'

    nid = Column(Integer, primary_key=True, autoincrement=True)  # id
    user_info_id = Column(Integer, ForeignKey('userinfo.nid'))  # 用户ID,外键 userinfo.nid
    news_id = Column(Integer, ForeignKey('news.nid'))
    ctime = Column(TIMESTAMP)  # 创建时间

    # 联合唯一的约束
    __table_args__ = (
        UniqueConstraint('user_info_id', 'news_id', name='uix_uid_nid'),
    )


class Comment(Base):
    """评论表"""
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


def session():
    # 创建DBSession类型:
    session = sessionmaker(bind=ENGINE)
    return session()

def init_db():
    # 创建所有表结构
    Base.metadata.create_all(ENGINE)

def drop_db():
    # 删除所有表构
    Base.metadata.drop_all(ENGINE)

def main():
    # drop_db()
    init_db()
    # pass


if __name__ == '__main__':
    main()
