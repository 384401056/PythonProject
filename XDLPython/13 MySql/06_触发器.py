#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

'''
定义触发器，触发的创建与存储过程类似，只是它主要定义的是在 增、删、改 之前和之后进行的自动执行的程。其中它有两处特殊的
关键字，NEW、OLD. NEW代指在增、改数据时，新的数据。OLD代指在改、删数据时，原来的数据。

delimiter $$ -- 定义结束符
DROP TRIGGER IF EXISTS tri_before_insert_tb_color ; 

# 创建触发器（在tb_color表插入操作之前的触发器），
CREATE TRIGGER tri_before_insert_tb_color BEFORE INSERT ON tb_color FOR EACH ROW
BEGIN
	INSERT INTO tb_dept(dept_name) VALUES(NEW.color_name); -- NEW是指在tb_color中插入的数据。
	                                                       -- OLD是指在对表的数据进行更新和删除时，原来的数据。
END $$
delimiter ; -- 恢复原有结束符

'''

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db = 'test', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 当在tb_color表中执行插入语句是，就会在这之前执行触发器的内容。
cursor.execute("INSERT INTO tb_color(color_name) VALUES(%s)", ('神谷科技',))

# for item in ret:
#     print(item)


# 提交修改
conn.commit()
cursor.close()
conn.close()


def main():
    pass


if __name__ == '__main__':
    main()
