#!/usr/bin/env python
# -*- coding utf-8 -*-

import time
import datetime


def f1():
    '''time的sleep功能'''
    print('slepp zzzzzz')
    time.sleep(3)
    print("wake up.....")


def f2():
    print(time.time())  # 返回系统的时间戳(从1970年开始到现在的秒数)
    print(time.ctime())  # 返回系统时间
    print(time.ctime(time.time() - 86400))  # ctime()还可模拟时间戳返回时间
    time_obj = time.gmtime()  # 返回struct_time的UTC时间.
    print(time_obj)
    print(time.localtime())  # 返回struct_time的本地时区时间.
    print(time.mktime(time.localtime()))  # 将struct_time转为时间戳格式
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))  # 将struct_time格式化.
    '''将字符串转为时间对象'''
    print(time.strptime('2017年10月10日 12点23分49秒', '%Y年%m月%d日 %H点%M分%S秒'))


def f3():
    print(datetime.date.today())  # 返回当前日期
    print(datetime.date.fromtimestamp(time.time()))  # 蒋时间戳转为日期格式.

    '''返回当前时间的datetime对象'''
    currentime = datetime.datetime.now()
    print(currentime)
    print(currentime.replace(2888, 10, 10))  # 将日期格式用输入的参数来替代。
    print(currentime.timetuple())  # 将datetime对象转为struct_time格式

    '''datetime 模块的字符和日期之间的互转'''
    print(datetime.date.strftime(currentime, '%Y-%m-%d %H:%M:%S'))
    print(datetime.datetime.strptime('2017年10月10日 12点23分49秒', '%Y年%m月%d日 %H点%M分%S秒'))


def f4():
    '''时间的加减'''
    now_date1 = datetime.datetime.now() - datetime.timedelta(days=10)  # 在当前时间上减去10天
    now_date2 = datetime.datetime.now() - datetime.timedelta(weeks=1)  # 在当前时间上减去1周
    now_date3 = datetime.datetime.now() - datetime.timedelta(hours=12)  # 在当前时间上减去12小时

    print(time.strftime('%Y-%m-%d %H:%M:%S', now_date1.timetuple()))
    print(datetime.date.strftime(now_date2, '%Y-%m-%d %H:%M:%S'))
    print(now_date3)


def main():
    f3()


if __name__ == '__main__':
    main()
