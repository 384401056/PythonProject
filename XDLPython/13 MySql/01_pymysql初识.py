#!/usr/bin/env python
# -*- coding utf-8 -*-

import pymysql


def main():
    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test')

    # 创建游标
    # cursor = conn.cursor()
    # 设置游标的返回类型为字典
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 执行SQL语句,返回受影响行数
    effect_row = cursor.execute("select * from tb_user")

    # 修改数据
    effect_row = cursor.execute("UPDATE tb_user  set department = 'IT'")

    # 插入数据(使用占位符，所有MySql数据类型都是用%s)
    effect_row = cursor.execute("INSERT into tb_user(tb_user.`name`,tb_user.age,tb_user.department,tb_user.`like`) VALUES(%s, %s, %s, %s)",
                                ('Jack', 20, 'CCO', 'shopping'))

    # 插入多条数据 executemany
    effect_row = cursor.executemany(
        "INSERT into tb_user(tb_user.`name`,tb_user.age,tb_user.department,tb_user.`like`) VALUES(%s, %s, %s, %s)",
        [('aaa',20,'bbb','ccc'),('uuu',20,'iii','nnn')])


    # 查询数据,返回的数据会存入cursor中
    cursor.execute("select * from tb_user")

    # 返回查询的所有数据, 此时要对cursor进设备，让其返回字典格式的数据。
    ret = cursor.fetchall()
    for item in ret:
        print(item)

    # 返回查询的第一条数据，同时游标下移.
    ret = cursor.fetchone()
    print(ret)
    ret = cursor.fetchone()
    print(ret)

    # 返回查询的指定条数据，同时游标下移.
    ret = cursor.fetchmany(5)
    print(ret)


    '''游标的移动操作'''
    cursor.scroll(2)
    ret = cursor.fetchone()

    # 相对当前位置上移。负数为上移，正数为下移
    cursor.scroll(-1, mode='relative')
    ret = cursor.fetchone()
    print(ret)

    # 以绝对位置移动.
    cursor.scroll(0, mode='absolute') # 移动至第一条数据
    ret = cursor.fetchone()
    print(ret)
    cursor.scroll(1, mode='absolute') # 移动至第二条数据
    ret = cursor.fetchone()
    print(ret)

    # 增加完数据后，获取最后一条数据的自增ID
    effect_row = cursor.execute("INSERT into tb_user(tb_user.`name`,tb_user.age,tb_user.department,tb_user.`like`) VALUES(%s, %s, %s, %s)",
                                ('pppppppppppp', 80, 'ppppp','ppppp'))
    print(cursor.lastrowid)
    # 提交修改
    conn.commit()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
