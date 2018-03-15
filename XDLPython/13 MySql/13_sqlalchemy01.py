#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-17 10:45:10
# @Author  : Gaoyanbin (gaoyanbin@agrithings.cn)
# @Link    : ${link}
# @Version : $Id$

import pymysql
from sqlalchemy import create_engine, false
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

'''
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
 
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
 
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
 
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
'''

Base = declarative_base()  # 生成一个sqlORM的基类.


class User(Base):
    '''创建ORM'''

    # 定义表名
    __tablename__ = 'tb_myuser'

    # 定义字段属性
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))
    age = Column(Integer)
    address = Column(String(100))

    # 输出格式
    def __repr__(self):
        return "id: %d, name: %s, age: %d, address: %s" % (self.id, self.name, self.age, self.address)


def main():
    # 创建数据库engine
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/chouti")
    # 创建所有表结构
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
