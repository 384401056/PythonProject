#!/usr/bin/env python
# -*- coding utf-8 -*-

import pymysql


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 对有外键关系的两张表，进行连表查询。left join 用外键去关联的表在左边
    cursor.execute("SELECT * FROM tb_user LEFT JOIN tb_dept ON department = tb_dept.id WHERE dept_name = '产品部'")
    # 对有外键关系的两张表，进行连表查询。right join  用外键去关联的表在右边(效果同上，只是返回的列的顺序有变化)
    cursor.execute("SELECT * FROM tb_dept RIGHT JOIN tb_user ON department = tb_dept.id WHERE dept_name = '产品部'")

    # 只显示所有有关联的数据。
    cursor.execute("SELECT * FROM tb_user INNER JOIN tb_dept ON department = tb_dept.id")

    # 多个外键的关联查询。
    cursor.execute("SELECT * FROM tb_user INNER JOIN tb_dept ON department = tb_dept.id INNER JOIN tb_color ON color = tb_color.id")
    cursor.execute("SELECT * FROM tb_dept RIGHT JOIN tb_user ON department = tb_dept.id RIGHT JOIN tb_color ON color = tb_color.id WHERE dept_name = '产品部'")

    ret = cursor.fetchall()
    for item in ret:
        print(item)

    # 提交修改
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
