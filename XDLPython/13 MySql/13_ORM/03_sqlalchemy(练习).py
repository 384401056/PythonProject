#!/usr/bin/env python
# -*- coding utf-8 -*-
from _ast import Index

from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建ORM基类
Base = declarative_base()
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test2?charset=utf8")  # echo为显示打印sql语句


class Clazz(Base):
    __tablename__ = 'tb_class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(50))

    def __repr__(self):
        return "Class(cid = %d, caption = %S" % (self.cid, self.caption)


class Student(Base):
    __tablename__ = 'tb_student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    gender = Column(String(2))
    class_id = Column(Integer, ForeignKey("tb_class.id"))

    def __repr__(self):
        return "Student(sid = %d, name = %S, gender = %s, class_id = %d" % (
            self.sid, self.name, self.gender, self.class_id)


class Teacher(Base):
    __tablename__ = 'tb_teacher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))

    def __repr__(self):
        return "Teacher(tid = %d, name = %S" % (self.tid, self.name)


class Course(Base):
    __tablename__ = 'tb_course'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    teacher_id = Column(Integer, ForeignKey('tb_teacher.id'))

    def __repr__(self):
        return "course(cid = %d, name = %S, teacher_id = %s" % (self.tid, self.name, self.teacher_id)


class Score(Base):
    __tablename__ = 'tb_score'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('tb_student.id'))
    course_id = Column(Integer, ForeignKey('tb_course.id'))
    number = Column(Integer)

    def __repr__(self):
        return "Score(sid = %d, student_id = %d, course_id = %d, number = %d" % (
            self.sid, self.student_id, self.course_id, self.number)


def create_table():
    '''创建所有表结构'''
    Base.metadata.create_all(engine)


def main():
    # create_table()
    '''

    查询物理成绩比生物成绩好的学生

    SELECT t1.student_id, sw_num, wl_num from

    (SELECT
        tb_score.student_id,
        tb_score.number AS sw_num,
      tb_course.`name`
    FROM tb_score
    LEFT JOIN tb_course ON tb_score.course_id = tb_course.id
    WHERE
        tb_course.`name` = '生物') as t1

    LEFT JOIN

    (SELECT
        tb_score.student_id,
        tb_score.number AS wl_num,
      tb_course.`name`
    FROM tb_score
    LEFT JOIN tb_course ON tb_score.course_id = tb_course.id
    WHERE
        tb_course.`name` = '物理') as t2

    ON t1.student_id = t2.student_id
    WHERE  t2.wl_num > if(ISNULL(t1.sw_num),0,t1.sw_num)

    '''







    # 创建DBSession类型:
    # MySession = sessionmaker(bind=engine)
    # session = MySession()
    #
    # ret = session.query(Student).filter(Student.name == "gaoyanbin1").count()
    #
    # print(ret)
    #
    # # 关闭session
    # session.close()


if __name__ == '__main__':
    main()
