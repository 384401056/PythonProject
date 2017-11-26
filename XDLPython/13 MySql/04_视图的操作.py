#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

'''
CREATE VIEW v1 AS SELECT * from tb_user 创建视图

SELECT * FROM v1 where id >=14 使用视图，与查表操作一致.

ALTER VIEW v1 AS SELECT * FROM tb_user WHERE id > 15  修改视图

DROP VIEW v1 删除视图
'''

def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


    cursor.execute("SELECT * FROM v1 where id >=14")

    ret = cursor.fetchall()
    for item in ret:
        print(item)

    # 提交修改
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()

