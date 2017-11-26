#!/usr/bin/env python
# -*- coding utf-8 -*-

import pymysql

'''pymsql生成的sql语句已经做了防止sql注入的机制。'''


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 通过以下方法，可以查看pymysql生成的原始sql语句
    query = cursor.mogrify("SELECT * FROM tb_user where name = %s and age = %s", ('Jim', 23))
    print(query)
    cursor.execute("SELECT * FROM tb_user where name = %s and age = %s", ('Jim', 23))

    ret = cursor.fetchall()
    for item in ret:
        print(item)

    # 提交修改
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
