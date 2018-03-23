#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
import time

BASE_DIR = str(os.path.dirname(os.path.dirname(__file__)))  # 获取当前文件所在文件夹的父路径
# BASE_DIR = str(os.path.dirname(__file__)) # 获取前文件的绝对路径
FILE_PATH = BASE_DIR + "/db_config.ini"

# 配置文件解析
cf = cparser.ConfigParser()
cf.read(FILE_PATH)

host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')
db = cf.get('mysqlconf', 'db_name')


class MySqlDB:
    '''封装Mysql的基体操作'''
    def __init__(self):
        try:
            self.conn = connect(
                host=host,
                user=user,
                password=password,
                db=db,
                charset='utf8mb4',
                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print('Mysql Error %d %s', (e.args[0], e.args[1]))

    def clear(self, table_name):
        '''清空表'''
        real_sql = 'delete from' + table_name + ';'
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')  # 禁用外键约束
            cursor.execute(real_sql)  # 执行sql语句
        self.conn.commit()  # 提交修改

    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())  # 将序列中的元素key以指定的字符连接生成一个新的字符串
        value = ','.join(table_data.values())  # 将序列中的元素value以指定的字符连接生成一个新的字符串

        print('key:',key)
        print('value:',value)

        # INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"

        print('realsql:'+real_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)

        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = MySqlDB()
    table_name = 'sign_event'
    data = {
        'name':'格力手机发布会',
        'limit':10000,
        'status':1,
        'address':'北京水立方',
        'start_name':'2018-12-23 14:00:00',
        'create_time':
    }
    db.insert(table_name, data)
    db.close()



