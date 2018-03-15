#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

'''
-- mysql内置函数的调用.
SELECT CHAR_LENGTH('李白'), LENGTH('李白'),CONCAT('字符','串','拼接');

'''

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("SELECT CHAR_LENGTH('李白')")  # 统计字符长度
cursor.execute("SELECT LENGTH('李白')")  # 统计字符的字节长度
cursor.execute("SELECT CONCAT('字符','串','拼接')")  # 字符串的拼接
cursor.execute("SELECT CONCAT_WS('__','字符','串','拼接')")  # 字符串的拼接,第一个参数为指定连接符

ret = cursor.fetchall()
print(ret)

# 提交修改
conn.commit()
cursor.close()
conn.close()
