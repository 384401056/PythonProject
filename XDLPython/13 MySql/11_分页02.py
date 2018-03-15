#!/usr/bin/env python
# -*- coding utf-8 -*-

import pymysql


def main():

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("INSERT INTO tb_page(tb_page.`name`, tb_page.age, tb_page.address) VALUES(%s,%s,%s)",
                   ('name_%d' % i[0], 100 + i[0], 'Yun Jing Rd 168,Economic and technical Development District'))
    cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()



if __name__ == '__main__':
    main()
