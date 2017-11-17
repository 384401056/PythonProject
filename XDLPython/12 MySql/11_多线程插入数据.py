#!/usr/bin/env python
# -*- coding utf-8 -*-

import pymysql
from MyThreadPool import *
import time
from multiprocessing import Process, Pool


def work(i):
    try:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO tb_page(tb_page.`name`, tb_page.age, tb_page.address) VALUES(%s,%s,%s)",
                       ('name_%d' % i[0], 100 + i[0], 'Yun Jing Rd 168,Economic and technical Development District'))
        cursor.fetchall()
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()
        print('down', i[0])


def down(status, result):
    pass



def create_data(num):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    for i in range(num):
        cursor.execute("INSERT INTO tb_page(tb_page.`name`, tb_page.age, tb_page.address) VALUES(%s,%s,%s)",
                       ('name_%d' % i, 100 + i, 'Yun Jing Rd 168,Economic and technical Development District'))
        cursor.fetchall()
        conn.commit()
        print('down ', i)
    cursor.close()
    conn.close()


def create_data_multhread(num):
    pool = MyThreadPool(1000)  # 用1000个线程
    for i in range(num):  # 执行1000个任务。（每个任务耗时1秒）
        pool.run(func=work, args=(i,), callback=down)
    pool.close()


def proce_work(i):
    try:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO tb_page(tb_page.`name`, tb_page.age, tb_page.address) VALUES(%s,%s,%s)",
                       ('name_%d' % i, 100 + i, 'Yun Jing Rd 168,Economic and technical Development District'))
        cursor.fetchall()
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()
        # print('down', i)
        return i

def proce_down(result):
    print('down', result)

def create_data_mulproce(num):
    pool = Pool(4)  # 定义进程池，并设置最大进程数。
    for i in range(num):
        # 开启进程
        # pool.apply(func=func01, args=(i,))
        pool.apply_async(func=proce_work, args=(i,), callback=proce_down)  # 并发执行进程，并可以设置回调函数。

    pool.close()
    pool.join()
    print('pool end')

def main():

    start_time = time.time()
    # create_data_mulproce(10000)
    create_data_multhread(10000)
    # create_data(10000)

    end_time = time.time()
    print('time is : %d' % (end_time - start_time))



if __name__ == '__main__':
    main()
