#!/usr/bin/env python
# -*- coding utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建ORM基类
Base = declarative_base()

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8")  # echo为显示打印sql语句


class Student(Base):
    __tablename__ = 'tb_student'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义主键，和自增长.
    name = Column(String(20))
    age = Column(Integer)
    address = Column(String(100))

    def __repr__(self):
        return "(id=%d,name=%s,age=%d,address=%s)" % (self.id, self.name, self.age, self.address)


def main():
    # 创建所有表结构
    # Base.metadata.create_all(engine)
    # 删除所有表结构
    # Base.metadata.drop_all(engine)

    # 创建DBSession类型:
    MySession = sessionmaker(bind=engine)
    session = MySession()

    # 插入单条数据
    student = Student(name='gaoyanbin', age=20, address='云南昆明')
    session.add(student)

    # 插入多条数据
    session.add_all([
    	Student(name='gaoyanbin1', age=21, address='云南昆明1'),
    	Student(name='gaoyanbin2', age=22, address='云南昆明2'),
    	Student(name='gaoyanbin3', age=23, address='云南昆明3'),
    	Student(name='gaoyanbin4', age=24, address='云南昆明4'),
    	])
    session.commit()

    ret = session.query(Student).all()
    ret = session.query(Student).filter(Student.name == 'gaoyanbin').one()
    ret = session.query(Student).filter(Student.name.in_(['gaoyanbin', 'gaoyanbin1', 'gaoyanbin4'])).all()
    # ~ 代表取反
    ret = session.query(Student).filter(~Student.name.in_(['gaoyanbin', 'gaoyanbin1', 'gaoyanbin4'])).all()
    # count() 计算数量
    ret = session.query(Student).filter(Student.name == "gaoyanbin1").count()
    print(ret)

    # 关闭session
    session.close()


if __name__ == '__main__':
    main()
