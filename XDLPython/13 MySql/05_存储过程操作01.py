#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

'''
创建存储过程
CREATE PROCEDURE proc_p1()
BEGIN
	SELECT * FROM tb_user;
END

删除存储过程
drop procedure proc_p1;
DROP PROCEDURE if EXISTS proc_p1 先判断是否存在，存在则删除。

调用存储过程
call proc_p1


delimiter $$ -- 定义结束符
CREATE PROCEDURE proc_p2(in il int) -- 定义参数
BEGIN
	DECLARE d1 int; -- 定义变量
	DECLARE d2 int DEFAULT 4;
	set d1 = il+d2;
	SELECT * from tb_user WHERE id = d1;
END $$
delimiter ; -- 恢复原有结束符

'''

def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


    # cursor.execute("call proc_p1")
    cursor.execute("call proc_p2(12)")

    ret = cursor.fetchall()
    for item in ret:
        print(item)

    # 提交修改
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()

