#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

'''
delimiter $$ -- 定义结束符
DROP PROCEDURE if EXISTS proc_p3;
CREATE PROCEDURE proc_p3(
	in i1 int,
	out i2 int -- 存储过程的返回变量
)
BEGIN
	set i2 = i1 + 100;
END $$
delimiter ; -- 恢复原有结束符


call proc_p3(5, @u);
SELECT @u;

==========================================

delimiter $$ -- 定义结束符
DROP PROCEDURE if EXISTS proc_p3;
CREATE PROCEDURE proc_p3(
	in i1 int,
	out i2 int, -- 存储过程的返回变量
	inout i3 int  -- 既可以当返回值，又可传入参数
)
BEGIN
	set i2 = i1 + 100; -- out结果
	SELECT * from tb_user; -- 查询结果
END $$
delimiter ; -- 恢复原有结束符

set @currage =18; -- 设置第三个参数。
call proc_p3(5, @u, @currage); -- 传入参数及要接收out变量人变量。


'''


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 执行存储过程,将传入参数.out参数可随意传值。只要参数个数对就可以。
    cursor.callproc('proc_p3', (5, 0, 20,))

    # 1.获取存储过程的查询返回值。
    ret = cursor.fetchall()
    for item in ret:
        print(item)

    # 2.获取存储过程的参数,也就是存储过程的返回值。
    cursor.execute("SELECT @_proc_p3_0, @_proc_p3_1, @_proc_p3_2")
    row = cursor.fetchone()
    print(row)

    # 提交修改
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
