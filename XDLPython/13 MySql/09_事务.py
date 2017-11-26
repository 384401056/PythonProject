#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

'''
pymsql 默认就支持事务。commit之前的sql都执行成功才会提交。
'''
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 对表中的jack减去100元
cursor.execute("UPDATE tb_account set overage = overage-100 WHERE account = 'jack'")
# 对表中的rose加上100元
cursor.execute("UPDATE tb_account set overage = overage+100 WHERE account = 'rose';")


conn.commit()
cursor.close()
conn.close()
