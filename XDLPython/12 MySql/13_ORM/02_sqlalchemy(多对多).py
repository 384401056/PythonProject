#!/usr/bin/env python
# -*- coding utf-8 -*-
from _ast import Index

from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建ORM基类
Base = declarative_base()
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8")  # echo为显示打印sql语句


'''多对多关联的建立'''

class Group(Base):
    __tablename__ = 'tb_group'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义主键，和自增长.
    name = Column(String(20), index=True)


class Server(Base):
    __tablename__ = 'tb_server'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义主键，和自增长.
    name = Column(String(20), index=True)


class ServerToGroup(Base):
    __tablename__ = 'tb_servertogroup'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义主键，和自增长.
    group_id = Column(Integer, ForeignKey('tb_group.id'))
    server_id = Column(Integer, ForeignKey('tb_server.id'))


def main():
    # 创建所有表结构
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
