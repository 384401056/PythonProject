#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

'''
函数有返回值，但是不能返回结果集。


-- 自定义函数
delimiter $$ -- 定义结束符
DROP FUNCTION IF EXISTS func_f1 ; 
CREATE FUNCTION func_f1(
	i1 int, -- 参数
	i2 int
) RETURNS int -- 返回值类型,注意这里是returns
BEGIN
	DECLARE num int;
	set num = i1 + i2;
	RETURN(num);
END $$
delimiter ; -- 恢复原有结束符

'''

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行函数
# cursor.execute("SELECT func_f1(12,34)")
# 可以把sql语句查询字段，当做参数传入函数中，并且每一行查询出的数据都会执行一次函数。
cursor.execute("SELECT func_f1(1,id), id FROM tb_user")

ret = cursor.fetchall()
for item in ret:
    print(item)

conn.commit()
cursor.close()
conn.close()
