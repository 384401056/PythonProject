#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import time
import getpass
import msvcrt, sys
from SendEmail import SendEmail
from HTMLTestRunner import HTMLTestRunner

PROJECT_NAME = 'WEB测试项目'
TEST_DIR = '.\\test_case'

# 根据目录和查找条件，自动发现测试用例.用例的加载顺序是根据ASCII码表的顺序。
discover = unittest.defaultTestLoader.discover(TEST_DIR, 'test*.py', None)


def find_new_report(file_dir):
    '''筛选出最新的测试报告'''
    reports = os.listdir(file_dir)  # 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
    reports.sort(key=lambda fn: os.path.getmtime(file_dir + '\\' + fn))
    # key = lambda fn: os.path.getmtime(file_dir + '\\' + fn)
    # print(reports)
    return os.path.join(file_dir, reports[-1])  # 返回最新的测试报告文件名和路径


if __name__ == '__main__':
    filename = PROJECT_NAME+time.strftime('%Y-%m-%d %H-%M-%S')+'_result.html'
    with open('./reports/'+filename, 'wb') as fb:
       runner = HTMLTestRunner(stream=fb,title='测试报告',description='用例执行情况')
       runner.run(discover)

    # pwd = input("Please input your password:")
    #
    # new_file = find_new_report('.\\reports')
    #
    # sender = SendEmail(PROJECT_NAME, new_file, pwd)
    # sender.send()
