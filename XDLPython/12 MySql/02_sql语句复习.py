#!/usr/bin/env python
# -*- coding utf-8 -*-

import pymysql


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 执行SQL语句,返回受影响行数
    # cursor.execute("select * from tb_user")
    # ret = cursor.fetchall()

    # in
    cursor.execute("SELECT * FROM tb_user WHERE id in(%s,%s)", (14, 15))

    # 分页
    cursor.execute("SELECT * FROM tb_user LIMIT %s OFFSET %s", (2, 1))  # 从1条开始，查找出后2条数据
    cursor.execute("SELECT * FROM tb_user LIMIT %s,%s", (1, 2))  # 功能同上

    # 排序
    cursor.execute("SELECT * FROM tb_user ORDER BY id ASC")  # 以id字段升序排列
    cursor.execute("SELECT * FROM tb_user ORDER BY id DESC")  # 降序排列

    # 分组
    cursor.execute("SELECT department,COUNT(*) FROM tb_user GROUP BY department ")  # 统计数量
    cursor.execute("SELECT department,COUNT(*) FROM tb_user GROUP BY department HAVING COUNT(*) >=2")  # 聚合统计数量大于2的

    # 跨表
    cursor.execute("SELECT * FROM tb_user WHERE id in (SELECT id FROM tb_user_other)")

    # 别名
    cursor.execute("SELECT `name` as n, age as a, department as d FROM tb_user")





    ret = cursor.fetchall()

    print(ret)

    # 提交修改
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
