#!/usr/bin/env python
# -*- coding utf-8 -*-
from _ast import Index

from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建ORM基类
Base = declarative_base()

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8")  # echo为显示打印sql语句


class College(Base):
    __tablename__ = 'tb_College'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义主键，和自增长.
    name = Column(String(20), index=True)  # index 普通索引


class Learner(Base):
    __tablename__ = 'tb_learner'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义主键，和自增长.
    name = Column(String(20), index=True)  # index 普通索引
    age = Column(Integer, unique=True)  # 唯一索引
    address = Column(String(100)),
    college_id = Column(Integer, ForeignKey('tb_College.id'))  # 外键,一对多

    # __tableagrs__ = (
    #     Index(name, address),  # 普通联合索引
    #     UniqueConstraint('id', 'name', name='uix_id_name')  # 联合唯一索引.索引名uix_id_name
    # )

    def __repr__(self):
        return "(id=%d,name=%s,age=%d,address=%s)" % (self.id, self.name, self.age, self.address)


def main():
    # 创建所有表结构
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
