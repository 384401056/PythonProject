#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

def create_test_data():
    '''创建测试数据'''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 创建1百万条测试数据。
    for i in range(1000000):
        cursor.execute("INSERT INTO tb_page(tb_page.`name`,tb_page.age,tb_page.address) VALUES(%s,%s,%s)",
                       ('name_%d' % i, 20 + i, '云南省昆明市经济技术开发区云景路168号银河科技园H栋3楼'))

    ret = cursor.fetchall()
    print(ret)

    # 提交修改
    conn.commit()
    cursor.close()
    conn.close()

def page():
    '''
    SSELECT countt(id) FROM tb_page # 先找出数据总条数

    # 查出以100为开始的页，的所有id (100为每页开头的id，可以通过数据总条数,当前是第几页，每页多少条计算得出.)
    SELECT id FROM tb_page WHERE id>100 ORDER BY id ASC LIMIT 100

    #能过上一个sql的结果，查出最大的id号是哪个。
    SELECT id FROM (SELECT id FROM tb_page WHERE id>100 ORDER BY id ASC LIMIT 100) as A ORDER BY id DESC LIMIT 1

    #根据上一个sql的结果，查出id<=最大的id号的所有数据
    SELECT * FROM tb_page WHERE id <= (SELECT id FROM (SELECT id FROM tb_page WHERE id> 50000 ORDER BY id ASC LIMIT 100) as A ORDER BY id DESC LIMIT 1) ORDER BY id DESC LIMIT 100

    #对上一个sql查出的数据进行排序。
    SELECT * FROM (SELECT * FROM tb_page WHERE id <= (SELECT id FROM (SELECT id FROM tb_page WHERE id> 50000 ORDER BY id ASC LIMIT 100) as A ORDER BY id DESC LIMIT 1) ORDER BY id DESC LIMIT 100) as A ORDER BY id ASC
    '''
    pass


def main():
    pass


if __name__ == '__main__':
    main()